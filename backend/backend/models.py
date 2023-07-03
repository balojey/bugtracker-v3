from beanie import Document, Link, BackLink
from typing import Optional
from pydantic import Field
from datetime import datetime
from fastapi_users.db import BeanieBaseUser
from .auth.models import OAuthAccount
from .roles import Role
from .priority import Priority
from .status import Status, ProjectStatus


class User(BeanieBaseUser, Document):
    first_name: str
    last_name: str
    role: Role
    comments: Optional[list[Link["Comment"]]] = Field(default_factory=list)
    bugs_to_fix: Optional[list[Link["Bug"]]] = Field(default_factory=list)
    project_members: Optional[list[Link["ProjectMember"]]] = Field(default_factory=list)
    reported_bugs: Optional[list[Link["Bug"]]] = Field(default_factory=list)
    assigned_roles: Optional[list[Link["ProjectMember"]]] = Field(default_factory=list)
    created_projects: Optional[list[Link["Project"]]] = Field(default_factory=list)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    oauth_accounts: list[OAuthAccount] = Field(default_factory=list)


class Project(Document):
    """Project model"""

    name: str
    description: str | None = None
    bugs: Optional[list[Link["Bug"]]] = Field(default_factory=list)
    created_by: BackLink["User"] = Field(original_field="created_projects")
    project_members: Optional[list[Link["ProjectMember"]]] = Field(default_factory=list)
    status: ProjectStatus
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Bug(Document):
    """Bug model"""

    title: str
    description: str | None = None
    steps_to_reproduce: str | None = None
    priority: Priority
    status: Status
    comments: Optional[list[Link["Comment"]]] = Field(default_factory=list)
    assigned_developer: Optional[BackLink["User"]] = Field(original_field="bugs_to_fix")
    reporter: BackLink["User"] = Field(original_field="reported_bugs")
    files: Optional[list[Link["File"]]] = Field(default_factory=list)
    project: Optional[BackLink["Project"]] = Field(original_field="bugs")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class Comment(Document):
    """Comment model"""

    content: str
    author: BackLink["User"] = Field(original_field="comments")
    bug: BackLink["Bug"] = Field(original_field="comments")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class File(Document):
    """Comment model"""

    filename: str
    url: str
    bug: BackLink["Bug"] = Field(original_field="files")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


class ProjectMember(Document):
    """ProjectMember model"""

    user: BackLink["User"] = Field(original_field="project_members")
    project: BackLink["Project"] = Field(original_field="project_members")
    assigned_by: BackLink["User"] = Field(original_field="assigned_roles")
    role: Role
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
