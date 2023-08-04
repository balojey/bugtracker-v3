import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from .bugs_by_status import *


def project_bugs():
    """Project bugs"""
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.flex(
            rx.box(
                new_bugs(),
                text_align="left",
                flex_grow=1,
                flex_basis="15%",
            ),
            rx.box(
                in_progress_bugs(),
                text_align="left",
                flex_grow=1,
                flex_basis="15%",
            ),
            rx.box(
                resolved_bugs(),
                text_align="left",
                flex_grow=1,
                flex_basis="15%",
            ),
            rx.box(
                closed_bugs(),
                text_align="left",
                flex_grow=1,
                flex_basis="15%",
            ),
            margin_top="16px",
            justify_content="space-around",
            align_items="flex-start",
            padding="1em",
            gap="8",
        ),
    )
