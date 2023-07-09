from pydantic import BaseModel, Field
from beanie.odm.fields import PydanticObjectId
from datetime import datetime


class CommentIn(BaseModel):
    """Comment model"""

    content: str


class CommentOut(CommentIn):
    """Comment model"""

    id: PydanticObjectId = Field(..., alias="_id")
    author: object
    created_at: datetime
    updated_at: datetime


class CommentUpdate(CommentIn):
    """Comment model"""

    pass
