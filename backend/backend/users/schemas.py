import uuid
from pydantic import Field
from fastapi_users import schemas
from ..roles import Role


class UserRead(schemas.BaseUser[uuid.UUID]):
    first_name: str
    last_name: str
    role: Role
    comments: list | None = []
    bugs_to_fix: list | None = []
    project_members: list | None = []
    reported_bugs: list | None = []
    assigned_roles: list | None = []
    created_projects: list | None = []


class UserCreate(schemas.BaseUserCreate):
    first_name: str
    last_name: str
    role: Role


class UserUpdate(schemas.BaseUserUpdate):
    first_name: str
    last_name: str
    # role: Role
