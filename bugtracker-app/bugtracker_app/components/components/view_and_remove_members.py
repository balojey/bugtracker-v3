import reflex as rx
from ...states import ManageProjectUsersState
from .view_project import view_project


def view_and_remove_members(**props):
    """View and remove members"""

    return rx.box(
        rx.foreach(ManageProjectUsersState.projects, view_project),
        width="100%",
    )