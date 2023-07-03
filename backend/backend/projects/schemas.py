from pydantic import BaseModel, Field
from beanie.odm.fields import PydanticObjectId, BackLink
from datetime import datetime
from ..users.schemas import UserRead
from ..models import User
from ..status import ProjectStatus


class ProjectIn(BaseModel):
    """Project model"""

    name: str
    description: str | None = None
    status: ProjectStatus


class ProjectOut(ProjectIn):
    """Project model"""

    id: PydanticObjectId = Field(..., alias="_id")
    created_by: BackLink[User]    # BackLink[User] = Field(..., alias="created_projects")
    created_at: datetime
    updated_at: datetime


class ProjectUpdate(ProjectIn):
    """Project model"""

    pass
