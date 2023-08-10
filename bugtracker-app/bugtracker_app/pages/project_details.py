import reflex as rx
from ..components.components import base_layout
from ..states import ProjectDetailsState


def project_details_heading(**props) -> rx.Component:
    """Project details heading"""

    return rx.box(
        rx.box(
            rx.heading("Details for ", ProjectDetailsState.title, size="lg"),
            rx.hstack(
                rx.link("Back to list", href="/my-projects"),
                rx.text(" | "),
                rx.cond(
                    ProjectDetailsState.is_admin,
                    rx.link("Edit", href="/edit-project"),
                    rx.cond(
                        ProjectDetailsState.is_assigned_admin,
                        rx.link("Edit", href="/edit-project"),
                    ),
                ),
            ),
        ),
        rx.table(
            rx.thead(
                rx.tr(
                    rx.th("Project Name"),
                    rx.th("Description"),
                )
            ),
            rx.tbody(
                rx.tr(
                    rx.td(ProjectDetailsState.title),
                    rx.td(ProjectDetailsState.description),
                )
            ),
        ),
        width="100%",
        **props,
    )


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
                        rx.td(rx.link("More details", href="/ticket-details")),
                    ),
                ),
            ),
        ),
        width="100%",
        **props,
    )


def project_details():
    """Project details page"""

    return base_layout(
        rx.box(
            project_details_heading(margin_bottom="3em"),
            rx.box(
                assigned_members(),
                ticket_list(),
                display="grid",
                grid_template_columns="1fr 2fr",
                gap="3em",
            ),
            width="100%",
            padding="3em",
        )
    )
