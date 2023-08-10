import reflex as rx
from ...states import ProjectDetailsState


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
