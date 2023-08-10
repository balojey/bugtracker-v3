import reflex as rx
from ...states import ProjectDetailsState


def assigned_members(**props) -> rx.Component:
    """Assigned members"""

    return rx.box(
        rx.heading("Assigned Members", size="lg"),
        rx.text("Members assigned to this project."),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Name"),
                    rx.th("Email"),
                    rx.th("Role"),
                )
            ),
            rx.tbody(
                rx.foreach(
                    ProjectDetailsState.members,
                    lambda member: rx.tr(
                        rx.td(member.full_name),
                        rx.td(member.email),
                        rx.td(member.role),
                    ),
                ),
            ),
        ),
        width="100%",
        **props,
    )
