"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from .styles import styles
from .pages import login_page
from .states import State
from .components.components import header

import reflex as rx


def index() -> rx.Component:
    return rx.box(
        header(),
        rx.vstack(
            rx.link(
                "Login",
                href="/login",
            )
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
app.compile()
