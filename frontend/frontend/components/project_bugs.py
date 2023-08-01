import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from .bugs_by_status import *


def project_bugs():
    """Project bugs"""
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.grid(
            rx.grid_item(new_bugs(), row_span=1, col_span=1, bg="lightgreen"),
            rx.grid_item(in_progress_bugs(), row_span=1, col_span=1, bg="lightblue"),
            rx.grid_item(resolved_bugs(), row_span=1, col_span=1, bg="purple"),
            rx.grid_item(closed_bugs(), row_span=1, col_span=1, bg="orange"),
            template_columns="repeat(4, 1fr)",
            h="10em",
            width="100%",
            gap=4,
            margin="50px 0",
        ),
    )
