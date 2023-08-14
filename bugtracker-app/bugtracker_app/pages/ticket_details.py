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
            rx.hstack(
                rx.vstack(
                    rx.heading("TICKET TYPE", size="sm"),
                    rx.text(ProjectTicketState.ticket_ticket_type),
                ),
                rx.vstack(
                    rx.heading("DESCRIPTION", size="sm"),
                    rx.text(ProjectTicketState.ticket_description),
                ),
                justify="space-between",
            ),
            rx.hstack(
                rx.vstack(
                    rx.heading("ASSIGNED DEVELOPER", size="sm"),
                    rx.text(ProjectTicketState.ticket_assigned_developer.full_name),
                ),
                rx.vstack(
                    rx.heading("SUBMITTER", size="sm"),
                    rx.text(ProjectTicketState.ticket_submitter.full_name),
                ),
                justify="space-between",
            ),
            rx.hstack(
                rx.vstack(
                    rx.heading("PROJECT", size="sm"),
                    rx.text(ProjectTicketState.ticket_project),
                ),
                rx.vstack(
                    rx.heading("PRIORITY", size="sm"),
                    rx.text(ProjectTicketState.ticket_priority),
                ),
                justify="space-between",
            ),
            rx.hstack(
                rx.vstack(
                    rx.heading("STATUS", size="sm"),
                    rx.text(ProjectTicketState.ticket_status),
                ),
                rx.vstack(
                    rx.heading("TICKET TYPE", size="sm"),
                    rx.text(ProjectTicketState.ticket_ticket_type),
                ),
                justify="space-between",
            ),
            rx.hstack(
                rx.vstack(
                    rx.heading("CREATED ON", size="sm"),
                    rx.text(ProjectTicketState.ticket_created_at),
                ),
                rx.vstack(
                    rx.heading("UPDATED ON", size="sm"),
                    rx.text(ProjectTicketState.ticket_updated_at),
                ),
                justify="space-between",
            ),
            margin_y="2em",
        ),
        **props,
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
    )


def ticket_history(**props) -> rx.Component:
    """Ticket history"""
    return rx.text("Ticket history")


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
