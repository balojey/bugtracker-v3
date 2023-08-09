from .base import State
from ..models import Project, User
import reflex as rx


class ManageProjectUsersState(State):
    """Manage project users state"""

    project_members: list[User] = []

    def handle_add_user(self, project_id: str, user_id: str):
        """Handle add user"""
        with rx.session() as session:
            project = session.query(Project).get(project_id)
            user = session.query(User).get(user_id)
            project.members.append(user)
            session.add(project)
            session.commit()
            session.refresh(project)

    def handle_remove_user(self, project_id: str, user_id: str):
        """Handle remove user"""
        with rx.session() as session:
            project = session.query(Project).get(project_id)
            user = session.query(User).get(user_id)
            project.members.remove(user)
            session.add(project)
            session.commit()
            session.refresh(project)

    @rx.var
    def projects(self) -> list[Project]:
        """Get projects"""
        with rx.session() as session:
            return session.query(Project).all()

    def get_members(self, project_id: str) -> list[User]:
        """Get members"""
        self.project_members = []
        with rx.session() as session:
            project = session.query(Project).get(project_id)
            self.project_members = project.members
