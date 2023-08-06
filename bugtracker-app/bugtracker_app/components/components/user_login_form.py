from ...states import LoginState
import reflex as rx


def user_login(**props) -> rx.Component:
    """User login Component"""
    return rx.box(
        rx.heading("Log in with your email", size="md"),
        rx.form(
            rx.vstack(
                rx.input(placeholder="Email", name="email", id="email", type="email"),
                rx.input(
                    placeholder="Password",
                    name="password",
                    id="password",
                    type="password",
                ),
                rx.button("Login", type_="submit"),
            ),
            on_submit=LoginState.handle_user_login,
        ),
        **props,
    )
