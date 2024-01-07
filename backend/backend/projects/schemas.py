from pydantic import BaseModel, Field
from typing import Optional, Union
from beanie.odm.fields import PydanticObjectId, BackLink
from datetime import datetime
from users.schemas import UserRead
from models import User
from status import ProjectStatus
from project_members.schemas import ProjectMemberOut


class ProjectIn(BaseModel):
    """Project model"""

    name: str
    description: Union[str, None] = None


class ProjectOut(ProjectIn):
    """Project model"""

    id: PydanticObjectId = Field(..., alias="_id")
    created_by: object
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(ProjectIn):
    """Project model"""

    pass
