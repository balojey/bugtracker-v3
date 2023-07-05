from fastapi import APIRouter, HTTPException, status, Depends
from fastapi_users import FastAPIUsers
import uuid
from ..models import User
from ..users.user_manager import get_user_manager
from ..auth.backend import auth_backend
from .schemas import ProjectMemberIn, ProjectMemberOut, ProjectMemberUpdate
from .utils import edit_project_member_role


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
router = APIRouter(prefix="/project_members", tags=["project_members"])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.patch("/{project_member_id}", response_model=ProjectMemberOut)
async def update_project_member(project_member_id: str, project_member: ProjectMemberUpdate, user: User = Depends(current_active_verified_user)):
    """A route to update a project member"""
    try:
        return await edit_project_member_role(project_member_id, project_member)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
