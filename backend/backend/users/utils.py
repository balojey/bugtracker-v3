from fastapi_users.db import BeanieUserDatabase
from pydantic import EmailStr
from models import User


async def get_user_db():
    yield BeanieUserDatabase(User)


async def find_user_by_id(id: str):
    """A function to find user by email"""
    user = await User.get(id)
    if not user:
        raise Exception("User does not exist")
    return user
