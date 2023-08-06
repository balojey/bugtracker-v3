import reflex as rx
from sqlmodel import Field
from uuid import uuid4
from datetime import datetime


def generateId() -> str:
    """Generate a random UUID4. and return it as a string."""
    return str(uuid4())


def getCurrentTime() -> str:
    """Get the current time."""
    return str(datetime.utcnow())


class BaseModel(rx.Model):
    """Base Model"""

    id: str = Field(default_factory=generateId, primary_key=True)
    created_at: str = Field(default_factory=getCurrentTime)
    updated_at: str = Field(default_factory=getCurrentTime)
