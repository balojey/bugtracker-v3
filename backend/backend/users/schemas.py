import uuid
from pydantic import Field, BaseModel
from datetime import datetime
from fastapi_users import schemas
from beanie.odm.fields import PydanticObjectId, Link
from ..models import ProjectMember
from ..roles import Role


class UserRead(schemas.BaseUser[PydanticObjectId]):
    first_name: str
    last_name: str
    role: Role
    created_at: datetime
    updated_at: datetime


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    role: Role


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    role: Role
