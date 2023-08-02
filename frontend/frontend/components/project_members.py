import reflex as rx
from ..states.dashboard_state import DashBoardPageState


def project_members():
    """The project members component"""
    return rx.box(
        rx.table_container(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Name"),
                        rx.th("Email"),
                        rx.th("Role"),
                        rx.cond(
                            DashBoardPageState.is_admin,
                            rx.th("Actions"),
                        ),
                    )
                ),
                rx.tbody(rx.foreach(DashBoardPageState.project_members, member)),
                variant="striped",
                color_scheme="teal",
            )
        ),
    )


def member(project_member: dict):
    """The project member component"""
    return rx.tr(
        rx.td(project_member["user"]),
        rx.td(project_member["email"]),
        rx.td(project_member["role"]),
        rx.cond(
            DashBoardPageState.is_admin,
            rx.td(
                rx.button(
                    rx.icon(tag="edit"),
                ),
                rx.button(rx.icon(tag="delete")),
            ),
        ),
    )
