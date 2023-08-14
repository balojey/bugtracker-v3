"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles import styles
from .pages import (
    login_page,
    dashboard,
    manage_project_users,
    my_projects,
    project_details,
    ticket_details,
)
from .states import State, DashBoardState, ProjectDetailsState, ProjectTicketState
from .components.components import home_header

import reflex as rx


def index() -> rx.Component:
    return rx.box(
        home_header(),
        rx.vstack(
            rx.link(
                "Dashboard",
                href="/dashboard",
            ),
            rx.link(
                "Manage project users",
                href="/manage-project-users",
            ),
            rx.link(
                "My projects",
                href="/projects",
            ),
        ),
        display="flex",
        justify_content="center",
        align_items="center",
        flex_direction="column",
        height="100vh",
        width="100vw",
    )


# Add state and page to the app.
app = rx.App(state=State, style=styles, stylesheets=["fonts/tenor_sans.css"])
app.add_page(index)
app.add_page(login_page, route="/login")
app.add_page(dashboard, route="/dashboard", on_load=DashBoardState.prepare_dashboard())
app.add_page(
    manage_project_users, route="/manage-project-users", on_load=State.check_login()
)
app.add_page(my_projects, route="/projects", on_load=State.check_login())
app.add_page(
    project_details,
    route="/projects/details",
    on_load=ProjectDetailsState.get_project_details(),
)
app.add_page(
    ticket_details,
    route="/projects/details/ticket",
    on_load=ProjectTicketState.get_ticket_details(),
)
app.compile()
