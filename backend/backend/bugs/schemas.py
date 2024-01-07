from pydantic import BaseModel, Field
from typing import Optional, Union
from datetime import datetime
from beanie.odm.fields import PydanticObjectId
from files.schemas import FileIn
from priority import Priority
from status import Status


class BugIn(BaseModel):
    """Bug model"""

    title: str
    description: Union[str, None] = None
    steps_to_reproduce: Union[str, None] = None
    priority: Priority = Priority.MEDIUM
    bug_files: Optional[list[FileIn]] = Field(default_factory=list)


class BugOut(BaseModel):
    """Bug model"""

    id: PydanticObjectId = Field(..., alias="_id")
    title: str
    description: Union[str, None] = None
    steps_to_reproduce: Union[str, None] = None
    priority: Priority
    status: Status
    assigned_developer: Optional[object]
    reporter: object
    assigner: Optional[object]
    project: object
    created_at: datetime
    updated_at: datetime


class BugUpdate(BaseModel):
    """Bug model"""

    title: str
    description: Union[str, None] = None
    steps_to_reproduce: Union[str, None] = None


class AssignedDeveloper(BaseModel):
    """AssignedDeveloper model"""

    id: str


class ChangePriority(BaseModel):
    """ChangePriorityAndStatus model"""

    priority: Priority = Priority.URGENT


class ChangeStatus(BaseModel):
    """ChangeStatus model"""

    status: Status = Status.RESOLVED
