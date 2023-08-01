from .sidebar_state import SideBarState
from ..schemas.roles import Role
from ..schemas.priority import PriorityReversed, Priority

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
    role: Role = Role.DEVELOPER
    report_bug_form_data: dict = {}
    priority: str = PriorityReversed.LOW.value

    def set_report_a_bug(self):
        self.report_a_bug = not self.report_a_bug

    def handle_add_project_member_submit(self, form_data: dict):
        """Handle add project member"""
        form_data["role"] = self.role
        self.add_project_member_form_data = form_data
        print(self.add_project_member_form_data)

    def handle_report_bug_form_data_submit(self, form_data: dict):
        """Handle report bug form data submit"""
        form_data["priority"] = priorities[self.priority]
        self.report_bug_form_data = form_data
        print(self.report_bug_form_data)
