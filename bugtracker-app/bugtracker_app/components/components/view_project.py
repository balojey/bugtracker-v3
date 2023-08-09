import reflex as rx
from ...states import ManageProjectUsersState
from .view_member import view_member


def view_project(project, **props):
    """View project"""

    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                rx.accordion_icon(),
                rx.heading(project.title, size="md"),
                on_click=lambda: ManageProjectUsersState.get_members(project.id),
            ),
            rx.accordion_panel(
                rx.foreach(ManageProjectUsersState.project_members, view_member)
            ),
        ),
        width="100%",
    )
