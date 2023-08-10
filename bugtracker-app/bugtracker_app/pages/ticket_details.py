import reflex as rx
from ..components.components import base_layout
from ..states import ProjectTicketState


def ticket_core_details(**props) -> rx.Component:
    """Ticket core details"""

    return rx.box(
        rx.heading("Details for ", size="md"),
        rx.link("Back to project", href="/projects/details"),
        rx.text(" | "),
        rx.cond(
            ProjectTicketState.is_admin,
            rx.link("Edit ticket", href="/projects/details/ticket/edit"),
            rx.cond(
                ProjectTicketState.is_assigned_admin,
                rx.link("Edit ticket", href="/projects/details/ticket/edit"),
            ),
        ),
        rx.box(
            rx.hstack(
                rx.heading("TICKET TYPE", size="sm"),
                rx.text(),
            ),
        ),
    )


def ticket_details():
    """Ticket details"""

    return base_layout(rx.box())
