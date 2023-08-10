from .base import State
from ..models import Project, User
from ..enumerations import Role
import reflex as rx


class Member(rx.Base):
    """Member"""

    id: str
    full_name: str
    role: Role


class ProjectSchema(rx.Base):
    """Project schema"""

    id: str
    title: str
    description: str
    creator_id: str
    members: list[Member]


class ManageProjectUsersState(State):
    """Manage project users state"""

    selected_project_members: list[User] = []
    selected_project_option: str = None
    selected_user_option: str = None

    # For viewing and removing users
    project_members_in_view: list[User] = []
    project_in_view: str = None

    def handle_remove_user(self, user_id: str):
        """Handle remove user"""
        with rx.session() as session:
            project = session.query(Project).get(self.project_in_view)
            user = session.query(User).get(user_id)
            project.members.remove(user)
            session.add(project)
            session.commit()
            session.refresh(project)

            for member in self.project_members_in_view:
                if member.id == user.id:
                    self.project_members_in_view.remove(member)
                    break

    @rx.var
    def projects(self) -> list[ProjectSchema]:
        """Get projects"""
        with rx.session() as session:
            projects = session.query(Project).all()
            for project in projects:
                project.members = project.members
        return projects

    def get_members(self, project_id: str):
        """Get project members"""
        self.project_members_in_view = []
        self.project_in_view = project_id
        with rx.session() as session:
            project = session.query(Project).get(project_id)
            self.project_members_in_view = project.members
        print(self.project_members_in_view)

    @rx.var
    def project_options(self) -> list:
        """Get project options"""
        with rx.session() as session:
            projects = session.query(Project).all()
            return [(project.id, project.title) for project in projects]

    def set_selected_project_option(self, option: tuple):
        """Set selected project option"""
        self.selected_project_option = option.split(",")[0]
        with rx.session() as session:
            project = session.query(Project).get(self.selected_project_option)
            if not project:
                self.selected_project_members = []
                return
            users = (
                session.query(User)
                .filter(User.id.notin_([member.id for member in project.members]))
                .all()
            )
            self.selected_project_members = [
                (user.id, user.full_name)
                for user in users
                if user.role != Role.ADMIN and user.role != Role.ASSIGNED_ADMIN
            ]

    def set_selected_user_option(self, option: tuple):
        """Set selected user option"""
        self.selected_user_option = option.split(",")[0]

    def handle_add_user(self):
        """Handle add user"""

        with rx.session() as session:
            if not self.selected_project_option or not self.selected_user_option:
                return rx.window_alert("Please select a project and a user")
            project = session.query(Project).get(self.selected_project_option)
            user = session.query(User).get(self.selected_user_option)
            project.members.append(user)
            session.add(project)
            session.commit()
            session.refresh(project)
            users = (
                session.query(User)
                .filter(User.id.notin_([member.id for member in project.members]))
                .all()
            )
            self.selected_project_members = [
                (user.id, user.full_name)
                for user in users
                if user.role != Role.ADMIN and user.role != Role.ASSIGNED_ADMIN
            ]
