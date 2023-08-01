import reflex as rx
from ..states.login_state import LoginPageState


def login():
    """The login page"""
    return rx.vstack(
        rx.vstack(
            rx.cond(
                LoginPageState.status,
                rx.alert(
                    rx.alert_icon(),
                    rx.alert_title(LoginPageState.message),
                    status=LoginPageState.status,
                ),
            ),
        ),
        rx.heading("Login", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="Email",
                        id="email",
                        type_="email",
                        is_required=True,
                    ),
                    rx.input(
                        placeholder="Password",
                        id="password",
                        type_="password",
                        is_required=True,
                    ),
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=LoginPageState.handle_submit,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(LoginPageState.form_data.to_string()),
    )
