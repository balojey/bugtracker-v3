import uuid
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from .user_manager import get_user_manager
from ..models import User
from ..auth.backend import auth_backend
from .schemas import UserRead, UserUpdate


fastapi_users = FastAPIUsers[User, uuid.UUID](get_user_manager, [auth_backend])


router = APIRouter()


router.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate, requires_verification=True),
    prefix="/users",
    tags=["users"],
)
