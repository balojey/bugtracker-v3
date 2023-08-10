import reflex as rx
from .auth import AuthState
from ..models import Project


class MyProjectState(AuthState):
    """State for my projects page."""

    project_id: str = ""

    @rx.var
    def projects(self) -> list[Project]:
        """List of projects."""
        with rx.session() as session:
            projects = session.query(Project).all()
            if self.is_admin or self.is_assigned_admin:
                return projects
            return [project for project in projects if self.user in project.members]

    def set_project_id(self, project_id: str):
        """Set project id."""
        self.project_id = project_id
