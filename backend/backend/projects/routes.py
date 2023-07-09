from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from beanie.odm.fields import PydanticObjectId
from ..models import User
from ..users.user_manager import get_user_manager
from ..auth.backend import auth_backend
from ..project_members.schemas import (
    ProjectMemberOut,
    ProjectMemberIn,
)
from ..project_members.utils import (
    write_project_member,
    fetch_project_members,
)
from ..permissions import (
    check_project_permission,
    check_user_presence_in_project,
)
from ..bugs.schemas import BugIn, BugOut

from ..bugs.utils import write_bug, read_bugs
from .utils import (
    write_project,
    read_project,
    edit_project,
    remove_project,
)
from .schemas import ProjectIn, ProjectOut, ProjectUpdate


fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
router = APIRouter(prefix="/projects", tags=["projects"])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: ProjectIn, user: User = Depends(current_active_verified_user)
):
    """A route to create a project"""
    try:
        return await write_project(user, project)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{project_id}", response_model=ProjectOut, status_code=status.HTTP_200_OK)
async def get_project(project_id: str):
    """A route to get a project"""
    try:
        return await read_project(project_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.patch(
    "/{project_id}", response_model=ProjectOut, status_code=status.HTTP_200_OK
)
async def update_project(
    project_id: str,
    project: ProjectUpdate,
    user: User = Depends(current_active_verified_user),
):
    """A route to update a project"""
    try:
        db_project = await read_project(project_id)
        if not db_project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        await check_project_permission(user, db_project)
        return await edit_project(db_project, project)
    except Exception as e:
        if str(e) == "Not enough permission":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.delete("/{project_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project(
    project_id: str, user: User = Depends(current_active_verified_user)
):
    """A route to delete a project"""
    try:
        project = await read_project(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        await check_project_permission(user, project)
        await remove_project(project)
    except Exception as e:
        if str(e) == "Not enough permission":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{project_id}/members",
    response_model=ProjectMemberOut,
    status_code=status.HTTP_201_CREATED,
)
async def add_project_member(
    project_id: str,
    project_member: ProjectMemberIn,
    user: User = Depends(current_active_verified_user),
):
    """A route to add a project member"""
    try:
        project = await read_project(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        await check_project_permission(user, project)
        return await write_project_member(user, project, project_member)
    except Exception as e:
        if str(e) == "Not enough permission":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        if str(e) == "Already a member":
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{project_id}/members", response_model=list[ProjectMemberOut])
async def get_project_members(project_id: str):
    """A route to get project members"""
    try:
        project = await read_project(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        return await fetch_project_members(project)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{project_id}/bugs", response_model=BugOut, status_code=status.HTTP_201_CREATED
)
async def add_project_bug(
    project_id: str, bug: BugIn, user: User = Depends(current_active_verified_user)
):
    """A route to add a bug to a project"""
    try:
        project = await read_project(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        await check_user_presence_in_project(user, project)
        return await write_bug(user, project, bug)
    except Exception as e:
        if str(e) == "You are not a member of this project":
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.get("/{project_id}/bugs", response_model=list[BugOut])
async def get_project_bugs(project_id: str):
    """A route to get project bugs"""
    try:
        project = await read_project(project_id)
        if not project:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project not found"
            )
        return await read_bugs(project)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
