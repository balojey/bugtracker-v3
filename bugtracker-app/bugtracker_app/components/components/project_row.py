import reflex as rx
from ...states import MyProjectState


def project_row(project, **props):
    """View project"""

    return rx.tr(
        rx.td(project.title),
        rx.td(project.description),
        rx.td(
            rx.list(
                rx.cond(
                    MyProjectState.is_admin,
                    rx.list_item(
                        rx.link(
                            "Manage users",
                            href="/manage-project-users",
                        )
                    ),
                    rx.cond(
                        MyProjectState.is_assigned_admin,
                        rx.list_item(
                            rx.link(
                                "Manage users",
                                href="/manage-project-users",
                            )
                        ),
                    ),
                ),
                rx.list_item(
                    rx.link(
                        "Details",
                        href="/projects/details",
                        on_click=MyProjectState.set_project_id(project.id),
                    )
                ),
            )
        ),
    )
