import reflex as rx
from ...states import AuthState


def header(**props) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.link(
                rx.heading(
                    "Bug Tracker",
                    size="lg",
                    background_image="linear-gradient(271.68deg, #EE756A 0.75%, #756AEE 88.52%)",
                    background_clip="text",
                ),
                href="/",
                _hover={"text_decoration": "none"},
            ),
            rx.cond(AuthState.logged_in, rx.text("Logged in as: ", AuthState.name)),
            margin_left="2em",
            # align_items="baseline",
        ),
        rx.hstack(
            rx.color_mode_button(rx.color_mode_icon()),
            rx.cond(
                AuthState.logged_in,
                rx.hstack(
                    rx.button("Logout", on_click=AuthState.logout),
                ),
                rx.hstack(
                    rx.button("Login", on_click=lambda: rx.redirect("/login")),
                ),
            ),
        ),
        display="flex",
        justify_content="space-between",
        align_items="center",
        padding=".2em",
        box_shadow="6px 20px 25px -21px rgba(40, 40, 40, 0.78)",
        **props,
    )
