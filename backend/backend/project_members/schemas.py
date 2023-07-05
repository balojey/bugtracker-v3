from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from beanie.odm.fields import PydanticObjectId
from ..roles import Role


class ProjectMemberIn(BaseModel):
    """ProjectMember model"""

    email: str
    role: Optional[Role]


class ProjectMemberOut(BaseModel):
    """ProjectMember model"""

    id: PydanticObjectId = Field(..., alias="_id")
    user: object
    # project: object
    # assigned_by: object
    role: Role
    created_at: datetime
    updated_at: datetime


class ProjectMemberUpdate(BaseModel):
    """ProjectMember model"""

    role: Role