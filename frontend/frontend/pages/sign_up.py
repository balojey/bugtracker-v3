from ..states.sign_up_state import SignUpPageState
import reflex as rx
from ..schemas.roles import Role, roles
from ..schemas.response_status import ResponseStatus


def sign_up_page():
    """The sign up page"""
    return rx.vstack(
        rx.vstack(
            rx.cond(
                SignUpPageState.status,
                rx.alert(
                    rx.alert_icon(),
                    rx.alert_title(SignUpPageState.message),
                    status=SignUpPageState.status,
                ),
            ),
        ),
        rx.heading("Signup", font_size="2em"),
        rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        placeholder="First Name",
                        id="first_name",
                        type_="text",
                        is_required=True,
                    ),
                    rx.input(
                        placeholder="Last Name",
                        id="last_name",
                        type_="text",
                        is_required=True,
                    ),
                ),
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
                rx.hstack(
                    rx.select(
                        roles,
                        placeholder="Select a role (default: Developer)",
                        on_change=SignUpPageState.set_role,
                    ),
                ),
                rx.button("Submit", type_="submit"),
            ),
            on_submit=SignUpPageState.handle_submit,
        ),
        rx.divider(),
        rx.heading("Results"),
        rx.text(SignUpPageState.form_data.to_string()),
    )
