import reflex as rx
from .state import State
import httpx
from ..schemas.status import BugStatus
from datetime import datetime
from ..schemas.roles import Role, ProjectMemberRole
from pprint import pprint


class ProjectIn(rx.Base):
    """Project In class"""

    name: str
    description: str
    _id: str
    created_by: object
    status: int
    created_at: datetime
    updated_at: datetime


class SideBarState(State):
    """The sidebar state."""

    project_member: dict = {}
    is_admin: bool = False
    is_project_manager: bool = False
    is_developer: bool = False
    is_qa_tester: bool = False
    create_project_state: bool = False
    project_form_data: dict = {}
    projects: list[dict] = []
    project_in_view_id: str | None = None
    project_in_view: dict = {}
    new_bugs: list[dict] = []
    in_progress_bugs: list[dict] = []
    resolved_bugs: list[dict] = []
    closed_bugs: list[dict] = []
    new_bugs_count: int = 0
    in_progress_bugs_count: int = 0
    resolved_bugs_count: int = 0
    closed_bugs_count: int = 0

    def handle_logout_click(self):
        """Handle the logout click event."""
        print(f"{self.token_type} {self.access_token}")
        self.reset()
        return rx.redirect("/")

    def change_create_project_state(self):
        self.create_project_state = not self.create_project_state

    def handle_project_form_submit(self, form_data: dict):
        """Handle project form submit"""
        self.project_form_data = form_data
        print("Auth: ", len(self.headers["Authorization"]))
        if len(self.headers["Authorization"]) < 10:
            return rx.redirect("/login")
        print("Project Form data: ", self.project_form_data)
        print("Headers: ", self.headers)
        response = httpx.post(
            f"{self.url}/projects/",
            headers=self.headers,
            json=self.project_form_data,
            follow_redirects=True,
        )
        print(response.json())
        return self.check_response(response.json(), response.status_code)

    def get_projects(self) -> None:
        """Get projects"""
        self.projects = []
        print("Auth: ", self.headers)
        print("Url: ", self.url)
        if len(self.headers["Authorization"]) < 10:
            return rx.redirect("/login")
        response = httpx.get(
            f"{self.url}/projects/", follow_redirects=True, headers=self.headers
        )
        print("Get projectsss response: ", response.json())
        self.projects.extend(response.json())

    def get_project(self, project_id: str) -> dict:
        """Get a project"""
        if len(self.headers["Authorization"]) < 10:
            return rx.redirect("/login")
        response = httpx.get(
            f"{self.url}/projects/{project_id}",
            follow_redirects=True,
            headers=self.headers,
        )
        print("Get project response: ", response.json())
        return response.json()

    def get_bugs(self, project_id: str) -> list[dict]:
        if len(self.headers["Authorization"]) < 10:
            return rx.redirect("/login")
        response = httpx.get(
            f"{self.url}/projects/{project_id}/bugs",
            follow_redirects=True,
            headers=self.headers,
        )
        print("Get bugs response: ", response.json())
        return response.json()

    def get_user_project_member(self, project_id):
        """Get user project member"""
        if len(self.headers["Authorization"]) < 10:
            return rx.redirect("/login")
        response = httpx.get(
            f"{self.url}/projects/{project_id}/members",
            follow_redirects=True,
            headers=self.headers,
        )
        current_user = httpx.get(
            f"{self.url}/users/me",
            follow_redirects=True,
            headers=self.headers,
        )
        current_user = current_user.json()
        self.me = current_user
        print("=======Current user: ", self.me)
        print("Get user project member response: ", response.json())
        for pm in response.json():
            pprint(pm)
            pprint(self.me)
            user = pm["user"]
            if user["email"] == self.me["email"]:
                self.project_member = pm
                if self.project_member["role"] == ProjectMemberRole.ADMIN.value:
                    self.is_admin = not self.is_admin
                elif (
                    self.project_member["role"]
                    == ProjectMemberRole.PROJECT_MANAGER.value
                ):
                    self.is_project_manager = not self.is_project_manager
                elif self.project_member["role"] == ProjectMemberRole.QA_TESTER.value:
                    self.is_qa_tester = not self.is_qa_tester
                else:
                    self.is_developer = not self.is_developer
                break

    def change_project_in_view(self, project_id: str):
        """Change project in view"""
        self.new_bugs, self.in_progress_bugs, self.resolved_bugs, self.closed_bugs = (
            [],
            [],
            [],
            [],
        )
        (
            self.new_bugs_count,
            self.in_progress_bugs_count,
            self.resolved_bugs_count,
            self.closed_bugs_count,
        ) = (0, 0, 0, 0)
        # ================================================= #
        self.project_in_view_id = project_id
        print("project_in_view_id: ", self.project_in_view_id)
        self.project_in_view = self.get_project(project_id)
        self.get_user_project_member(project_id)

        if self.project_in_view:
            self.project_in_view["created_at"] = datetime.strptime(
                self.project_in_view["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
            ).strftime("%B %d, %Y")

        print("project_in_view: ", self.project_in_view)
        bugs = self.get_bugs(project_id)
        print("bugs: ", bugs)
        if bugs:
            for bug in bugs:
                bug["updated_at"] = datetime.strptime(
                    bug["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
                ).strftime("%B %d, %Y")
                reporter = bug["reporter"]
                user = reporter["user"]
                bug["reporter"] = f"{user['first_name']} {user['last_name']}"
                if bug["status"] == BugStatus.NEW.value:
                    self.new_bugs_count += 1
                    self.new_bugs.append(bug)
                elif bug["status"] == BugStatus.IN_PROGRESS.value:
                    self.in_progress_bugs_count += 1
                    self.in_progress_bugs.append(bug)
                elif bug["status"] == BugStatus.RESOLVED.value:
                    self.resolved_bugs_count += 1
                    self.resolved_bugs.append(bug)
                else:
                    self.closed_bugs_count += 1
                    self.closed_bugs.append(bug)


def display_project_name(project: dict):
    return rx.text(
        project["name"],
        on_click=lambda x: SideBarState.change_project_in_view(project["_id"]),
    )
