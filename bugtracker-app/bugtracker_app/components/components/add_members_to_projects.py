import reflex as rx
from ...states import ManageProjectUsersState


def add_members_to_projects():
    """Add members to projects"""

    return rx.box(
        rx.heading("Add members to projects", size="md"),
        rx.form(
            rx.vstack(
                rx.select(
                    ManageProjectUsersState.project_options,
                    placeholder="Select a project",
                    on_change=ManageProjectUsersState.set_selected_project_option,
                    color_schemes="twitter",
                ),
                rx.select(
                    ManageProjectUsersState.selected_project_members,
                    placeholder="Select a user",
                    on_change=ManageProjectUsersState.set_selected_user_option,
                    color_schemes="twitter",
                ),
                rx.button("Add user", type_="submit"),
            ),
            on_submit=ManageProjectUsersState.handle_add_user,
        ),
    )
