from beanie import Document, Link
from typing import Optional
from pydantic import Field, HttpUrl
from datetime import datetime
from fastapi_users.db import BeanieBaseUser
from .auth.models import OAuthAccount
from .roles import Role, ProjectMemberRole
from .priority import Priority
from .status import Status, ProjectStatus


class User(BeanieBaseUser, Document):
    first_name: str
    last_name: str
    role: Role
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    oauth_accounts: list[OAuthAccount] = Field(default_factory=list)


class Project(Document):
    """Project model"""

    name: str
    description: str | None = None
    created_by: Link["User"]
    status: ProjectStatus = ProjectStatus.NEW
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Bug(Document):
    """Bug model"""

    title: str
    description: str | None = None
    steps_to_reproduce: str | None = None
    priority: Priority
    status: Status = Status.NEW
    assigned_developer: Optional[Link["ProjectMember"]]
    reporter: Link["ProjectMember"]
    assigner: Optional[Link["ProjectMember"]]
    project: Link["Project"]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Comment(Document):
    """Comment model"""

    content: str
    author: Link["ProjectMember"]
    bug: Link["Bug"]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class File(Document):
    """Comment model"""

    filename: str
    url: str
    bug: Link["Bug"]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectMember(Document):
    """ProjectMember model"""

    user: Link["User"]
    project: Link["Project"]
    role_assigned_by: Link["User"]
    role: ProjectMemberRole
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
