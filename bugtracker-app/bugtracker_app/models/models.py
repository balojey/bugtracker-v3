from .base_model import BaseModel
from pydantic import EmailStr
from ..enumerations import *
from sqlmodel import Field, Relationship
from typing import Optional


class UserProject(BaseModel, table=True):
    """User project model"""

    user_id: Optional[str] = Field(
        default=None, foreign_key="user.id", primary_key=True
    )
    project_id: Optional[str] = Field(
        default=None, foreign_key="project.id", primary_key=True
    )


class User(BaseModel, table=True):
    """User model"""

    full_name: str
    role: Optional[Role]
    email: EmailStr
    password: str
    projects: Optional[list["Project"]] = Relationship(
        back_populates="members", link_model=UserProject
    )


class Project(BaseModel, table=True):
    """Project model"""

    title: str
    description: str
    creator_id: str = Field(default=None, foreign_key="user.id")
    tickets: Optional[list["Ticket"]] = Relationship(back_populates="project")
    members: Optional[list["User"]] = Relationship(
        back_populates="projects", link_model=UserProject
    )


class Ticket(BaseModel, table=True):
    """Ticket model"""

    title: str
    description: str
    submitter_id: str = Field(default=None, foreign_key="user.id")
    project_id: str = Field(default=None, foreign_key="project.id")
    assigned_developer_id: Optional[str] = Field(default=None, foreign_key="user.id")
    ticket_type: TicketType
    priority: Priority
    status: Status
    attachments: Optional[list["Attachment"]] = Relationship(back_populates="ticket")
    history: Optional[list["TicketHistory"]] = Relationship(back_populates="ticket")
    project: Optional[Project] = Relationship(back_populates="tickets")
    comments: Optional[list["Comment"]] = Relationship(back_populates="ticket")


class Attachment(BaseModel, table=True):
    """Attachment model"""

    file_name: str
    description: str
    file_path: str
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
    ticket: Optional[Ticket] = Relationship(back_populates="attachments")


class TicketHistory(BaseModel, table=True):
    """Ticket history model"""

    action: Action
    previous_value: str
    present_value: str
    made_by: str = Field(default=None, foreign_key="user.id")
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
    ticket: Optional[Ticket] = Relationship(back_populates="history")


class Comment(BaseModel, table=True):
    """Comment model"""

    content: str
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
    ticket: Optional[Ticket] = Relationship(back_populates="comments")
    commenter_id: str = Field(default=None, foreign_key="user.id")
