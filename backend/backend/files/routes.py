from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_users import FastAPIUsers
from beanie.odm.fields import PydanticObjectId
from ..models import User
from ..auth.backend import auth_backend
from ..users.user_manager import get_user_manager
from ..permissions import check_bug_delete_permission
from .utils import read_attachment, remove_attachment


router = APIRouter(prefix="/files", tags=["files"])
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])
current_active_verified_user = fastapi_users.current_user(active=True, verified=True)


@router.delete("/{file_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_file(file_id: str, user: User = Depends(current_active_verified_user)):
    """Delete a file"""
    try:
        file = await read_attachment(file_id)
        if not file:
            raise Exception("File not found")
        await check_bug_delete_permission(user, file.bug)
        await remove_attachment(file)
    except Exception as e:
        if (
            str(e) == "You cannot delete this bug"
            or str(e)
            == "You cannot delete this bug because a developer has been assigned to this bug"
            or str(e) == "You are neither a manager nor an admin"
        ):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(e))
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e))
