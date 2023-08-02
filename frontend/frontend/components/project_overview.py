import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from datetime import datetime


def project_overview():
    return rx.box(
        rx.hstack(
            rx.hstack(
                rx.heading(
                    DashBoardPageState.project_in_view["name"],
                ),
                rx.text(
                    "Created on ",
                    DashBoardPageState.project_in_view["created_at"],
                    padding_top="12px",
                ),
            ),
            rx.spacer(),
            rx.hstack(
                rx.form(
                    rx.hstack(
                        rx.input(placeholder="Search", id="search", type_="text"),
                        rx.button("Search", bg="#000", color="#fff"),
                    ),
                ),
                rx.button(
                    rx.icon(tag="up_down"),
                    bg="#fff",
                    border="1px solid #eaeaea",
                ),
            ),
        ),
        margin_top="16px",
        margin_bottom="16px",
    )
