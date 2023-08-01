"""Welcome to Reflex! This file outlines the steps to create a basic app."""
from rxconfig import config
from .states.state import State
from .pages.sign_up import sign_up_page
from .pages.login import login
from .pages.dashboard import dashboard

import reflex as rx

docs_url = "https://reflex.dev/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


def index() -> rx.Component:
    return rx.fragment(
        rx.color_mode_button(rx.color_mode_icon(), float="right"),
        rx.vstack(
            rx.heading("Welcome to Reflex!", font_size="2em"),
            rx.box("Get started by editing ", rx.code(filename, font_size="1em")),
            rx.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": rx.color_mode_cond(
                        light="rgb(107,99,246)",
                        dark="rgb(179, 175, 255)",
                    )
                },
            ),
            spacing="1.5em",
            font_size="2em",
            padding_top="10%",
        ),
    )


# Add state and page to the app.
app = rx.App(state=State)
app.add_page(index)
app.add_page(
    sign_up_page,
    route="/signup",
    title="Sign Up",
    description="Sign up to bug tracker.",
)
app.add_page(login, route="/login", title="Login", description="Login to bug tracker.")
app.add_page(dashboard, route="/dashboard", title="Dashboard", description="Dashboard")
app.compile()
