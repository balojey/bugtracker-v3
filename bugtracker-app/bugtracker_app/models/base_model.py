import reflex as rx
from sqlmodel import Field
from uuid import uuid4
from datetime import datetime


def generateId():
    """Generate a random UUID4. and return it as a string."""
    return str(uuid4())


class BaseModel(rx.Model):
    """Base Model"""

    id: str = Field(default_factory=generateId, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
