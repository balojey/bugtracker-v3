"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles import styles
from .pages import login_page, dashboard
from .states import State, DashBoardState
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
app.compile()
