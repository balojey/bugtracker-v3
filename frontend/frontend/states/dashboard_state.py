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

    @rx.var
    def is_authenticated(self):
        """Is the user authenticated?"""
        return len(self.headers["Authorization"]) > 10

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
