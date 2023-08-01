import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from ..components.sidebar import sidebar
from ..components.project_overview import project_overview
from ..components.project_bugs import project_bugs
from ..components.dashboard_form import dashboard_form


def dashboard():
    """The dashboard page"""
    return rx.box(
        rx.hstack(
            sidebar(),
        ),
        rx.cond(
            DashBoardPageState.project_in_view_id,
            rx.vstack(
                project_overview(),
                dashboard_form(),
                project_bugs(),
                width="80%",
                max_width="100%",
                margin_left="auto",
            ),
            rx.heading(
                "Welcome to the dashboard",
                size="lg",
                margin_top="16px",
                width="80%",
                max_width="100%",
                margin_left="auto",
            ),
        ),
        padding="0px",
        margin="0px",
        width="100%",
    )
