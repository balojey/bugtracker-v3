from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_users import FastAPIUsers
import uuid
from ..models import User
from ..users.user_manager import get_user_manager
from ..auth.backend import auth_backend
from ..permissions import check_project_permission
from .schemas import ProjectMemberIn, ProjectMemberOut, ProjectMemberUpdate
from .utils import edit_project_member_role, read_project_member, remove_project_member

fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
router = APIRouter(prefix="/project_members", tags=["project_members"])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.patch("/{project_member_id}", response_model=ProjectMemberOut)
async def update_project_member(
    project_member_id: str,
    member_role: ProjectMemberUpdate,
    user: User = Depends(current_active_verified_user),
):
    """A route to update a project member"""
    try:
        db_project_member = await read_project_member(project_member_id)
        if not db_project_member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project member not found"
            )
        print(db_project_member.project)
        await check_project_permission(user, db_project_member.project)
        return await edit_project_member_role(user, db_project_member, member_role)
    except Exception as e:
        if str(e) == "Not enough permission":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        if str(e) == "Cannot edit project owner":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{str(e)}, Project owner role cannot be edited",
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
    

@router.delete("/{project_member_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_project_member(project_member_id: str, user: User = Depends(current_active_verified_user)):
    """A route to delete a project member"""
    try:
        project_member = await read_project_member(project_member_id)
        if not project_member:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Project member not found"
            )
        await check_project_permission(user, project_member.project)
        return await remove_project_member(project_member)
    except Exception as e:
        if str(e) == "Not enough permission":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        if str(e) == "Cannot edit project owner":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"{str(e)}, Project owner role cannot be edited",
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
