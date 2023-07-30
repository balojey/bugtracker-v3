from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from beanie.odm.fields import PydanticObjectId
from ..models import User
from ..auth.backend import auth_backend
from ..users.user_manager import get_user_manager
from ..project_members.utils import (
    read_project_member,
    fetch_project_member,
    fetch_project_member_by_user,
)
from ..comments.schemas import CommentOut, CommentIn
from ..comments.utils import write_comment, read_comments
from ..files.schemas import FileOut, FileIn
from ..files.utils import save_attachment, read_attachments
from ..permissions import (
    check_user_presence_in_project,
    check_bug_assignment_permission_for_user,
    check_reporter,
    check_bug_delete_permission,
    check_reporter_and_assigned_developer,
    check_assigned_developer,
)
from .schemas import BugOut, BugUpdate, AssignedDeveloper, ChangePriority, ChangeStatus
from .utils import (
    read_bug,
    edit_bug,
    assign_bug_to_developer,
    edit_bug_priority,
    edit_bug_status,
    remove_bug,
)


router = APIRouter(prefix="/bugs", tags=["bugs"])
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.get("/{bug_id}", response_model=BugOut, status_code=status.HTTP_200_OK)
async def get_bug(bug_id: str):
    """A route to get a bug"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        return bug
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{bug_id}", response_model=BugOut, status_code=status.HTTP_200_OK)
async def update_bug(
    bug_id: str, bug: BugUpdate, user: User = Depends(current_active_verified_user)
) -> BugOut:
    """A route to update a bug"""
    try:
        db_bug = await read_bug(bug_id)
        if not db_bug:
            raise Exception("Bug not found")
        await check_reporter(user, db_bug.reporter)
        return await edit_bug(db_bug, bug)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))


@router.patch(
    "/{bug_id}/assign-developer", response_model=BugOut, status_code=status.HTTP_200_OK
)
async def assign_developer(
    bug_id: str,
    developer: AssignedDeveloper,
    user: User = Depends(current_active_verified_user),
):
    """A route to assign a bug to a developer"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        await check_bug_assignment_permission_for_user(user, bug.project)
        developer = await read_project_member(developer.id)
        if not developer:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Developer not found"
            )
        # await check_developer_role_in_project(developer, bug.project)
        admin_or_project_manager = await fetch_project_member(user, bug.project)
        return await assign_bug_to_developer(bug, admin_or_project_manager, developer)
    except Exception as e:
        if (
            str(e) == "You are not a project manager or an admin of this project"
            or str(e) == "You are not a member of this project"
            or str(e) == "You are neither a manager nor an admin"
        ):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch(
    "/{bug_id}/priority", response_model=BugOut, status_code=status.HTTP_200_OK
)
async def update_priority(
    bug_id: str,
    bug_priority: ChangePriority,
    user: User = Depends(current_active_verified_user),
):
    """A route for changing a bug priority"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        await check_reporter_and_assigned_developer(
            user, bug.reporter, bug.assigned_developer
        )
        return await edit_bug_priority(bug, bug_priority)
    except Exception as e:
        if str(e) == "You cannot edit this bug":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch("/{bug_id}/status", response_model=BugOut, status_code=status.HTTP_200_OK)
async def update_status(
    bug_id: str,
    bug_status: ChangeStatus,
    user: User = Depends(current_active_verified_user),
):
    """A route for changing a bug priority"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        await check_assigned_developer(user, bug.assigned_developer)
        return await edit_bug_status(bug, bug_status)
    except Exception as e:
        if str(e) == "You cannot edit this bug":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{bug_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bug(bug_id: str, user: User = Depends(current_active_verified_user)):
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        await check_bug_delete_permission(user, bug)
        await remove_bug(bug)
    except Exception as e:
        if (
            str(e) == "You are not a project manager or an admin of this project"
            or str(e) == "You are not a member of this project"
            or str(e) == "You cannot delete this bug"
            or str(e)
            == "You cannot delete this bug because a developer has been assigned to this bug"
        ):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{bug_id}/comments", response_model=CommentOut, status_code=status.HTTP_201_CREATED
)
async def create_comment(
    bug_id: str, comment: CommentIn, user: User = Depends(current_active_verified_user)
):
    """A route for creating a comment"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        author = await fetch_project_member_by_user(user, bug.project)
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Author not found"
            )
        await check_user_presence_in_project(user, bug.project)
        return await write_comment(comment, bug, author)
    except Exception as e:
        if str(e) == "You are not a member of this project":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get(
    "/{bug_id}/comments",
    response_model=list[CommentOut],
    status_code=status.HTTP_200_OK,
)
async def get_comments(bug_id: str):
    """A route for getting all comments for a bug"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        return await read_comments(bug)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post("/{bug_id}/attachments", response_model=FileOut, status_code=status.HTTP_201_CREATED)
async def upload_attachment(
    bug_id: str, file: FileIn, user: User = Depends(current_active_verified_user)
):
    """A route for creating an attachment"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        await check_reporter(user, bug.reporter)
        return await save_attachment(file, bug)
    except Exception as e:
        if (
            str(e) == "You are not a member of this project"
            or str(e) == "You cannot edit this bug"
        ):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get(
    "/{bug_id}/attachments",
    response_model=list[FileOut],
    status_code=status.HTTP_200_OK,
)
async def get_attachments(bug_id: str):
    """A route for getting all attachments for a bug"""
    try:
        bug = await read_bug(bug_id)
        if not bug:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Bug not found"
            )
        return await read_attachments(bug)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
