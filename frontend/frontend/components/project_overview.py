import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from datetime import datetime


def project_overview():
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.hstack(
            rx.box(
                rx.flex(
                    rx.heading(
                        DashBoardPageState.project_in_view["name"],
                    ),
                    rx.text("Created on"),
                    rx.text(
                        DashBoardPageState.project_in_view["created_at"],
                    ),
                ),
            ),
            rx.box(
                rx.form(
                    rx.hstack(
                        rx.flex(
                            rx.input(placeholder="Search", id="search", type_="text"),
                            rx.button("Search", bg="#000", color="#fff"),
                        ),
                        rx.button(
                            rx.icon(tag="up_down"),
                            bg="#fff",
                            border="1px solid #eaeaea",
                        ),
                    ),
                ),
            ),
            margin_top="16px",
        ),
        rx.heading(
            "Welcome to the dashboard",
            size="lg",
            margin_top="16px",
        ),
    )
