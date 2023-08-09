from ..components.components import demo_user_login, user_login, home_header
import reflex as rx


def login_page() -> rx.Component:
    """Login Page"""
    return rx.box(
        home_header(),
        rx.heading("Login", size="lg"),
        rx.responsive_grid(
            user_login(flex_grow="1", padding_x="1em",),
            demo_user_login(flex_grow="1", padding_x="1em",),
            columns=[2],
            spacing="8",
        ),
        width="100vw",
        height="100vh",
        display="flex",
        justify_content="center",
        align_items="stretch",
        flex_direction="column",
    )
