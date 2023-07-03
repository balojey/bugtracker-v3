from pydantic import BaseModel, Field
from datetime import datetime


class FileIn(BaseModel):
    """File model"""

    filename: str
    url: str


class FileOut(FileIn):
    """File model"""

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime


class FileUpdate(FileIn):
    """File model"""

    pass
