import reflex as rx
from ...states import AuthState


def header(**props) -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading("Bug Tracker", size="lg", background_image="linear-gradient(271.)"),
            rx.cond(AuthState.logged_in, rx.text("Logged in as: ", AuthState.name)),
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
        position="absolute",
        top="0",
        width="100vw",
        padding=".2em",
    )
