import reflex as rx
from ...states import AuthState


links = [
    rx.link(
        rx.icon(tag="link"), "Dashboard", href="/dashboard", padding="1em", width="80%"
    ),
    rx.link(
        rx.icon(tag="link"),
        "Manage Role Assignment",
        href="/dashboard",
        padding="1em",
        width="100%",
    ),
    rx.link(
        rx.icon(tag="link"),
        "Manage Project Users",
        href="/dashboard",
        padding="1em",
        width="100%",
    ),
    rx.link(
        rx.icon(tag="link"),
        "My Projects",
        href="/dashboard",
        padding="1em",
        width="100%",
    ),
    rx.link(
        rx.icon(tag="link"),
        "My Tickets",
        href="/dashboard",
        padding="1em",
        width="100%",
    ),
    rx.link(
        rx.icon(tag="link"),
        "User Profile",
        href="/dashboard",
        padding="1em",
        width="100%",
    ),
]


def sidebar(**props):
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.avatar(name=AuthState.name, size="xl"),
                rx.vstack(
                    rx.heading(
                        "Welcome",
                        size="md",
                        text_align="left",
                    ),
                    rx.heading(
                        AuthState.name,
                        size="md",
                        text_align="left",
                    ),
                    align_items="flex-start",
                    justify_content="center",
                ),
                padding_x=".2em",
            ),
            rx.spacer(),
            rx.spacer(),
            rx.spacer(),
            rx.list(
                items=links,
                spacing="2.5em",
            ),
            margin="0",
        ),
        box_shadow="20px 0px 23px -8px rgba(40, 40, 40, 0.19)",
        padding_top="2em",
        **props,
    )
