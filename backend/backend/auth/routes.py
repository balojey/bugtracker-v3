from beanie.odm.fields import PydanticObjectId
from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from ..users.user_manager import get_user_manager
from ..models import User
from ..users.schemas import UserRead, UserCreate
from ..config import Settings
from .backend import auth_backend
from .oauth2 import google_oauth_client


settings = Settings()
fastapi_users = FastAPIUsers[User, PydanticObjectId](get_user_manager, [auth_backend])


router = APIRouter()


router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(UserRead), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_reset_password_router(), prefix="/auth", tags=["auth"]
)
router.include_router(
    fastapi_users.get_oauth_router(
        google_oauth_client,
        auth_backend,
        settings.secret_key,
        associate_by_email=True,
        is_verified_by_default=True,
    ),
    prefix="/auth/google",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_oauth_associate_router(
        google_oauth_client, UserRead, settings.secret_key
    ),
    prefix="/auth/associate/google",
    tags=["auth"],
)
