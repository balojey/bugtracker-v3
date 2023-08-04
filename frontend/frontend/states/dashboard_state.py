import reflex as rx
from .sidebar_state import SideBarState
from ..schemas.roles import Role
from ..schemas.priority import PriorityReversed, Priority
from datetime import datetime
import httpx

priorities = {
    PriorityReversed.LOW.value: Priority.LOW.value,
    PriorityReversed.MEDIUM.value: Priority.MEDIUM.value,
    PriorityReversed.HIGH.value: Priority.HIGH.value,
    PriorityReversed.URGENT.value: Priority.URGENT.value,
    PriorityReversed.IMMEDIATE.value: Priority.IMMEDIATE.value,
    PriorityReversed.CRITICAL.value: Priority.CRITICAL.value,
    PriorityReversed.BLOCKER.value: Priority.BLOCKER.value,
}


class DashBoardPageState(SideBarState):
    """The dashboard page state."""

    report_a_bug: bool = False
    add_project_member_form_data: dict = {}
    role: Role = Role.DEVELOPER.value
    report_bug_form_data: dict = {}
    priority: str = PriorityReversed.LOW.value
    img: list[str]
    bug_in_view: dict = {}
    bug_in_view_id: str | None = None
    bug_in_view_comments: list[dict] = []
    bug_in_view_comments_count: int = 0
    bug_in_view_attachments: list[dict] = []
    bug_in_view_attachments_count: int = 0
    view_bug: bool = False
    is_reporter: bool = False
    is_assigned_developer: bool = False

    @rx.var
    def is_authenticated(self):
        """Is the user authenticated?"""
        return len(self.headers["Authorization"]) > 10

    def set_view_bug(self):
        self.view_bug = not self.view_bug

    def set_bug_in_view(self, bug_id: str):
        """Set the bug in view"""
        self.set_view_bug()
        print("=============view_bug: ", self.view_bug)
        self.is_reporter = False
        self.is_assigned_developer = False
        self.bug_in_view_id = bug_id
        response = httpx.get(
            f"{self.url}/bugs/{self.bug_in_view_id}",
            headers=self.headers,
            follow_redirects=True,
        )
        print("======set_bug_in_view Response: ", response.json())
        self.bug_in_view = response.json()
        reporter = self.bug_in_view["reporter"]
        print("==============Reporter: ", reporter)
        developer = self.bug_in_view["assigned_developer"]
        print("==============Developer: ", developer)
        if reporter["user"]["email"] == self.me["email"]:
            print("=========I am the reporter==============")
            self.is_reporter = not self.is_reporter
        if developer:
            if developer["user"]["email"] == self.me["email"]:
                print("=========I am the developer==============")
                self.is_assigned_developer = not self.is_assigned_developer

    def set_bug_priority_color(self, priority: str | int) -> str:
        """Return the color of a priority value"""
        print("============set_bug_priority_color: ", priority)
        color = self.priority_colors[priority]
        return color

    def set_bug_priority_text(self, priority: str | int) -> str:
        """Return the text of a priority value"""
        print("============set_bug_priority_text: ", priority)
        text = self.priority_text[priority]
        return text

    async def handle_upload(self, files: list[rx.UploadFile]):
        """Handle the upload of file(s).

        Args:
            files: The uploaded files.
        """
        for file in files:
            upload_data = await file.read()
            outfile = rx.get_asset_path(file.filename)

            # Save the file.
            with open(outfile, "wb") as file_object:
                file_object.write(upload_data)

            # Update the img var.
            self.img.append(file.filename)

    def set_report_a_bug(self):
        self.report_a_bug = not self.report_a_bug

    def handle_add_project_member_submit(self, form_data: dict):
        """Handle add project member"""
        form_data["role"] = self.role
        self.add_project_member_form_data = form_data
        print(self.add_project_member_form_data)
        response = httpx.post(
            f"{self.url}/projects/{self.project_in_view_id}/members",
            follow_redirects=True,
            headers=self.headers,
            json=self.add_project_member_form_data,
        )
        print(response.status_code)
        print(response.json())
        if response.status_code == 404:
            return rx.window_alert("User with this email does not exist")
        if response.status_code == 409:
            return rx.window_alert("User is already a project member")
        if response.status_code == 201:
            return rx.window_alert("Role assigned")

    def handle_report_bug_form_data_submit(self, form_data: dict):
        """Handle report bug form data submit"""
        form_data["priority"] = priorities[self.priority]
        form_data["bug_files"] = []
        if self.img:
            for image in self.img:
                form_data["bug_files"].append({"filename": image, "url": ""})
        self.report_bug_form_data = form_data
        print(self.report_bug_form_data)
        response = httpx.post(
            f"{self.url}/projects/{self.project_in_view_id}/bugs",
            follow_redirects=True,
            headers=self.headers,
            json=self.report_bug_form_data,
        )
        print("handle_report_bug_form_data_submit Response: ", response.json())
        self.set_report_a_bug()
        self.img = []
