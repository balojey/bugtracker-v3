from sqlalchemy import ForeignKeyConstraint
from .base_model import BaseModel
from pydantic import EmailStr
from enumerations import *
from sqlmodel import Field, Relationship
from typing import Optional


class User(BaseModel, table=True):
    """User model"""

    first_name: str
    last_name: str
    email: EmailStr
    password: str
    projects: Optional[list["Project"]] = Relationship(back_populates="creator")
    projects_joined: Optional[list["ProjectMember"]] = Relationship(
        back_populates="assignee"
    )


class Project(BaseModel, table=True):
    """Project model"""

    name: str
    description: str
    creator_id: str = Field(default=None, foreign_key="user.id")
    creator: Optional[User] = Relationship(back_populates="projects")
    tickets: Optional[list["Ticket"]] = Relationship(back_populates="project")
    members: Optional[list["ProjectMember"]] = Relationship(back_populates="project")


class ProjectMember(BaseModel, table=True):
    """Project member model"""

    project_id: str = Field(default=None, foreign_key="project.id")
    assignee_id: str = Field(default=None, foreign_key="user.id")
    assigner_id: Optional[str] = Field(default=None, foreign_key="projectmember.id")
    role: Role
    project: Optional[Project] = Relationship(back_populates="members")
    assignee: Optional[User] = Relationship(back_populates="projects_joined")
    comments: Optional[list["Comment"]] = Relationship(back_populates="commenter")


class Ticket(BaseModel, table=True):
    """Ticket model"""

    title: str
    description: str
    submitter_id: str = Field(default=None, foreign_key="projectmember.id")
    project_id: str = Field(default=None, foreign_key="project.id")
    assigned_developer_id: Optional[str] = Field(
        default=None, foreign_key="projectmember.id"
    )
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
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
    ticket: Optional[Ticket] = Relationship(back_populates="history")


class Comment(BaseModel, table=True):
    """Comment model"""

    content: str
    ticket_id: str = Field(default=None, foreign_key="ticket.id")
    ticket: Optional[Ticket] = Relationship(back_populates="comments")
    commenter_id: str = Field(default=None, foreign_key="projectmember.id")
    commenter: Optional[ProjectMember] = Relationship(back_populates="comments")
