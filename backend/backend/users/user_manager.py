from datetime import datetime
from typing import Any, Dict, Optional, Union
from fastapi import Depends, Request, Response
from fastapi_users import (
    BaseUserManager,
    InvalidPasswordException,
    schemas,
)
from fastapi_users_db_beanie import ObjectIDIDMixin
from beanie.odm.fields import PydanticObjectId

from ..config import Settings
from .schemas import UserCreate, UserRead
from ..models import User
from .utils import get_user_db
from ..auth.password_hash import password_helper


settings = Settings()


class UserManager(ObjectIDIDMixin, BaseUserManager[User, PydanticObjectId]):
    reset_password_token_secret = settings.secret_key
    verification_token_secret = settings.secret_key

    async def validate_password(
        self, password: str, user: Union[UserCreate, User]
    ) -> None:
        if len(password) < 8:
            raise InvalidPasswordException(
                reason="Password should be at least 8 characters"
            )

        if password.isdigit():
            raise InvalidPasswordException(reason="Password should not be all numeric")

        if password.isalpha():
            raise InvalidPasswordException(
                reason="Password should not be all alphabetic"
            )

        if password.islower():
            raise InvalidPasswordException(
                reason="Password should contain at least one uppercase character"
            )

        if password.isupper():
            raise InvalidPasswordException(
                reason="Password should contain at least one lowercase character"
            )

        if password.isalnum():
            raise InvalidPasswordException(
                reason="Password should contain at least one special character"
            )

        if password.isspace():
            raise InvalidPasswordException(
                reason="Password should not contain any whitespace"
            )

        if password.isidentifier():
            raise InvalidPasswordException(
                reason="Password should not be a python identifier"
            )

        if password.isdecimal():
            raise InvalidPasswordException(reason="Password should not be a decimal")

        if password.isnumeric():
            raise InvalidPasswordException(reason="Password should not be a numeric")

        if user.email in password:
            raise InvalidPasswordException(
                reason="Password should not contain the email address"
            )

        if user.first_name in password:
            raise InvalidPasswordException(
                reason="Password should not contain the first name"
            )

        if user.last_name in password:
            raise InvalidPasswordException(
                reason="Password should not contain the last name"
            )

        if user.first_name.lower() in password.lower():
            raise InvalidPasswordException(
                reason="Password should not contain the first name"
            )

        if user.last_name.lower() in password.lower():
            raise InvalidPasswordException(
                reason="Password should not contain the last name"
            )

        if user.first_name.upper() in password.upper():
            raise InvalidPasswordException(
                reason="Password should not contain the first name"
            )

        if user.last_name.upper() in password.upper():
            raise InvalidPasswordException(
                reason="Password should not contain the last name"
            )

    async def on_after_update(
        self, user: User, update_dict: Dict[str, Any], request: Optional[Request] = None
    ):
        user.updated_at = datetime.utcnow()
        print(f"User {user.id} has been updated with {update_dict}")

    async def on_after_login(
        self,
        user: User,
        request: Optional[Request] = None,
        response: Optional[Response] = None,
    ):
        print(f"User {user.id} has logged in.")

    async def on_after_verify(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has been verified.")

    async def on_after_reset_password(
        self, user: User, request: Optional[Request] = None
    ):
        print(f"User {user.id} has reset their password.")

    async def on_before_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} is about to be deleted.")

    async def on_after_delete(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has been deleted.")

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")

    async def on_after_forgot_password(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"User {user.id} has forgot their password. Reset token: {token}")

    async def on_after_request_verify(
        self, user: User, token: str, request: Optional[Request] = None
    ):
        print(f"Verification requested for user {user.id}. Verification Token: {token}")
        user = await self.verify(token, request)
        user_schema = UserRead
        return schemas.model_validate(user_schema, user)


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db, password_helper)
