from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from ..roles import Role


class ProjectMemberIn(BaseModel):
    """ProjectMember model"""

    email: str
    role: Optional[Role]


class ProjectMemberOut(ProjectMemberIn):
    """ProjectMember model"""

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime


class ProjectMemberUpdate(ProjectMemberIn):
    """ProjectMember model"""

    pass