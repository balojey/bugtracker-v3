from pydantic import BaseModel, Field
from datetime import datetime
from ..priority import Priority
from ..status import Status


class BugIn(BaseModel):
    """Bug model"""

    title: str
    description: str | None = None
    steps_to_reproduce: str | None = None
    priority: Priority
    status: Status


class BugOut(BugIn):
    """Bug model"""

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime


class BugUpdate(BugIn):
    """Bug model"""

    pass


class AssignedDeveloper(BaseModel):
    """AssignedDeveloper model"""

    email: str
