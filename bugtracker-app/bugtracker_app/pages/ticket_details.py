import reflex as rx
from ..components.components import base_layout
from ..states import ProjectTicketState


def ticket_core_details(**props) -> rx.Component:
    """Ticket core details"""

    return rx.box(
        rx.heading("Details for ", ProjectTicketState.ticket_title, size="md"),
        rx.hstack(
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
        ),
        rx.box(
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("TICKET TITLE"),
                        rx.th("DESCRIPTION"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td(ProjectTicketState.ticket_title),
                        rx.td(ProjectTicketState.ticket_description),
                    )
                ),
            ),
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("ASSIGNED DEVELOPER"),
                        rx.th("SUBMITTER"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td(""),
                        rx.td(""),
                    )
                ),
            ),
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("PROJECT"),
                        rx.th("TICKET PRIORITY"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td(ProjectTicketState.ticket_project),
                        rx.td(ProjectTicketState.ticket_priority),
                    )
                ),
            ),
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("TICKET STATUS"),
                        rx.th("TICKET TYPE"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td(ProjectTicketState.ticket_status),
                        rx.td(ProjectTicketState.ticket_ticket_type),
                    )
                ),
            ),
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("CREATED ON"),
                        rx.th("UPDATED ON"),
                    )
                ),
                rx.tbody(
                    rx.tr(
                        rx.td(ProjectTicketState.ticket_created_at),
                        rx.td(ProjectTicketState.ticket_updated_at),
                    )
                ),
            ),
            margin_y="2em",
        ),
        **props,
        padding_x="2em",
        border_right="1px solid gray",
    )


def comment_section(**props) -> rx.Component:
    """Add and read comments"""

    return rx.box(
        rx.heading("Add a comment", size="md"),
        rx.form(
            rx.text_area(
                placeholder="Add a comment",
                rows=5,
                cols=50,
            ),
            rx.button("Add", type_="submit"),
            display="flex",
            align_items="baseline",
        ),
        rx.heading("Comments", size="md"),
        rx.text("All comments from this ticket"),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Commenter"),
                    rx.th("Message"),
                    rx.th("Commented on"),
                ),
            ),
            rx.tbody(
                rx.foreach(
                    ProjectTicketState.comments,
                    lambda comment: rx.tr(
                        rx.td(comment.commenter.full_name),
                        rx.td(comment.content),
                        rx.td(comment.created_at),
                    ),
                ),
            ),
        ),
        **props,
        padding_x="2em",
    )


def ticket_history(**props) -> rx.Component:
    """Ticket history"""
    return rx.box(
        rx.heading("Ticket History"),
        rx.text("All history information for the ticket"),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Action"),
                    rx.th("Previous Value"),
                    rx.th("Present Value"),
                    rx.th("Date Changed"),
                )
            ),
            rx.tbody(
                rx.foreach(
                    ProjectTicketState.get_history,
                    lambda history: rx.tr(
                        rx.td(history.action),
                        rx.td(history.previous_value),
                        rx.td(history.present_value),
                        rx.td(history.created_at),
                    ),
                )
            ),
        ),
    )


def attachment_section(**props) -> rx.Component:
    """Ticket attachments"""
    return rx.text("Ticket attachments")


def ticket_details():
    """Ticket details"""

    return base_layout(
        rx.box(
            ticket_core_details(),
            comment_section(),
            ticket_history(),
            attachment_section(),
            padding="3em",
            display="grid",
            grid_template_columns="1fr 1fr",
            grid_template_rows="1fr 1fr",
            gap="2em",
        )
    )
