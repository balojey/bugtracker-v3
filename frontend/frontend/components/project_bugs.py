import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from .bugs_by_status import *


def project_bugs():
    """Project bugs"""
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.flex(
            rx.spacer(),
            rx.box(new_bugs(), row_span=1, col_span=1, bg="lightgreen"),
            rx.spacer(),
            rx.box(in_progress_bugs(), row_span=1, col_span=1, bg="lightblue"),
            rx.spacer(),
            rx.box(resolved_bugs(), row_span=1, col_span=1, bg="purple"),
            rx.spacer(),
            rx.box(closed_bugs(), row_span=1, col_span=1, bg="orange"),
            rx.spacer(),
            width="100%",
            gap=4,
            margin="50px 0",
        ),
    )
