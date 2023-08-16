import reflex as rx
from ...states import ProjectDetailsState


def ticket_list(**props) -> rx.Component:
    """Ticket list"""

    return rx.box(
        rx.heading("Tickets", size="lg"),
        rx.text("Tickets for this project."),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Title"),
                    rx.th("Submitter"),
                    rx.th("Status"),
                    rx.th("Assigned To"),
                    rx.th("Submitted on"),
                )
            ),
            rx.tbody(
                rx.foreach(
                    ProjectDetailsState.tickets,
                    lambda ticket: rx.tr(
                        rx.td(ticket.title),
                        rx.td(ticket.submitter.full_name),
                        rx.td(ticket.status),
                        rx.td(ticket.assigned_developer.full_name),
                        rx.td(ticket.created_at),
                        rx.td(
                            rx.link(
                                "More details",
                                href="/projects/details/ticket",
                                on_click=lambda: ProjectDetailsState.set_ticket_id(
                                    ticket.id
                                ),
                            )
                        ),
                    ),
                ),
            ),
        ),
        **props,
    )
