import reflex as rx
from ...states import ManageProjectUsersState
from ...states.manage_project_users_state import ProjectSchema
from .view_member import view_member


def view_project(project, **props):
    """View project"""
    # print(project.members)

    return rx.accordion(
        rx.accordion_item(
            rx.accordion_button(
                rx.accordion_icon(),
                rx.heading(project.title, size="md"),
                on_click=lambda: ManageProjectUsersState.get_members(project.id),
            ),
            rx.accordion_panel(
                rx.foreach(ManageProjectUsersState.project_members_in_view, view_member)
            ),
        ),
        width="100%",
        allow_toggle=True,
        allow_multiple=False,
    )
