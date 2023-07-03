import uuid
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from ..models import User
from ..users.user_manager import get_user_manager
from ..auth.backend import auth_backend
from ..roles import Role
from ..users.schemas import UserRead
from ..project_members.schemas import (
    ProjectMemberOut,
    ProjectMemberUpdate,
    ProjectMemberIn,
)
from ..project_members.utils import write_project_member
from .utils import (
    write_project,
    read_project,
    edit_project,
    check_project_permission,
    remove_project,
)
from .schemas import ProjectIn, ProjectOut, ProjectUpdate


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])
router = APIRouter(prefix="/projects", tags=["projects"])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.post("/", response_model=ProjectOut, status_code=status.HTTP_201_CREATED)
async def create_project(
    project: ProjectIn, user: User = Depends(current_active_verified_user)
):
    """A route to create a project"""
    if user.role != Role.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You don't have permission to create a project",
        )
    try:
        return await write_project(user.id, project)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@router.get("/{project_id}", response_model=ProjectOut, status_code=status.HTTP_200_OK)
async def get_project(project_id: str):
    """A route to get a project"""
    try:
        return await read_project(project_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


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
        await check_project_permission(user, project_id)
        return await edit_project(project_id, project)
    except Exception as e:
        if e == "You don't have permission to access this project":
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
        await check_project_permission(user, project_id)
        await remove_project(project_id)
    except Exception as e:
        if e == "You don't have permission to access this project":
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=str(e),
            )
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))


@router.post(
    "/{project_id}/members",
    response_model=ProjectOut,
    status_code=status.HTTP_201_CREATED,
)
async def add_project_member(
    project_id: str,
    project_member: ProjectMemberIn,
    user: User = Depends(current_active_verified_user),
):
    """A route to add a project member"""
    pass
