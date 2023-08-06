from ...states import LoginState
import reflex as rx


demo_users = [
    rx.button(
        "DemoAdmin1",
        size="lg",
        on_click=lambda: LoginState.login_as_demo_user("demoadmin1"),
    ),
    rx.button(
        "DemoAdmin2",
        size="lg",
        on_click=lambda: LoginState.login_as_demo_user("demoadmin2"),
    ),
    rx.button(
        "DemoProjectManager1",
        size="lg",
        on_click=lambda: LoginState.login_as_demo_user("demoprojectmanager1"),
    ),
    rx.button(
        "DemoDeveloper1",
        size="lg",
        on_click=lambda: LoginState.login_as_demo_user("demodeveloper1"),
    ),
    rx.button(
        "DemoSubmitter1",
        size="lg",
        on_click=lambda: LoginState.login_as_demo_user("demosubmitter1"),
    ),
]

style = {
    rx.box
}


def demo_user_login(**props) -> rx.Component:
    """Demo user login Component"""
    return rx.box(
        rx.heading("Login as a predefined user", size="md"),
        rx.list(items=demo_users, spacing=".25em"),
        **props
    )
