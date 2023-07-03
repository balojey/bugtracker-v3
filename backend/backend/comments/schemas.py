from pydantic import BaseModel, Field
from datetime import datetime


class CommentIn(BaseModel):
    """Comment model"""

    content: str


class CommentOut(CommentIn):
    """Comment model"""

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime


class CommentUpdate(CommentIn):
    """Comment model"""

    pass
