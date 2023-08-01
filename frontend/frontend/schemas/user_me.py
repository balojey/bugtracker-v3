from pydantic import BaseModel
from datetime import datetime
from .roles import Role
import reflex as rx

class Me(rx.Base):
    id: int
    email: str
    is_active: bool
    is_superuser: bool
    is_verified: bool
    first_name: str
    last_name: str
    role: Role
    created_at: datetime
    updated_at: datetime
