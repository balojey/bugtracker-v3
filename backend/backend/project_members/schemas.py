from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from beanie.odm.fields import PydanticObjectId
from roles import ProjectMemberRole


class ProjectMemberIn(BaseModel):
    """ProjectMember model"""

    email: str
    role: ProjectMemberRole


class ProjectMemberOut(BaseModel):
    """ProjectMember model"""

    id: PydanticObjectId = Field(..., alias="_id")
    user: object
    project: object
    role: ProjectMemberRole
    role_assigned_by: object
    created_at: datetime
    updated_at: datetime


class ProjectMemberUpdate(BaseModel):
    """ProjectMember model"""

    role: ProjectMemberRole