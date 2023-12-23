from pydantic import BaseModel, Field, HttpUrl
from datetime import datetime
from beanie.odm.fields import PydanticObjectId


class FileIn(BaseModel):
    """File model"""

    filename: str
    url: HttpUrl


class FileOut(FileIn):
    """File model"""

    id: PydanticObjectId = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime


class FileUpdate(FileIn):
    """File model"""

    pass
