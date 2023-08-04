import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from .project_display_bug import project_display_new_bug


def new_bugs():
    """New bugs"""
    return rx.box(
        rx.heading(
            "New",
            size="md",
        ),
        rx.text(
            DashBoardPageState.new_bugs_count,
            " bugs available",
            margin_bottom="0.3em",
            margin_top="0.1em",
            font_size="0.8em",
            color="#999999",
        ),
        rx.divider(
            border_color="black", width="100%", height="1em", border_bottom="2px solid"
        ),
        rx.foreach(DashBoardPageState.new_bugs, project_display_new_bug),
    )


def in_progress_bugs():
    """New bugs"""
    return rx.box(
        rx.heading("In Progress", size="md"),
        rx.text(
            DashBoardPageState.in_progress_bugs_count,
            " bugs available",
            margin_bottom="0.3em",
            margin_top="0.1em",
            font_size="0.8em",
            color="#999999",
        ),
        rx.divider(
            border_color="black", width="100%", height="1em", border_bottom="2px solid"
        ),
        rx.foreach(DashBoardPageState.in_progress_bugs, project_display_new_bug),
    )


def resolved_bugs():
    """New bugs"""
    return rx.box(
        rx.heading("Resolved", size="md"),
        rx.text(
            DashBoardPageState.resolved_bugs_count,
            " bugs available",
            margin_bottom="0.3em",
            margin_top="0.1em",
            font_size="0.8em",
            color="#999999",
        ),
        rx.divider(
            border_color="black", width="100%", height="1em", border_bottom="2px solid"
        ),
        rx.foreach(DashBoardPageState.resolved_bugs, project_display_new_bug),
    )


def closed_bugs():
    """New bugs"""
    return rx.box(
        rx.heading("Closed", size="md"),
        rx.text(
            DashBoardPageState.closed_bugs_count,
            " bugs available",
            margin_bottom="0.3em",
            margin_top="0.1em",
            font_size="0.8em",
            color="#999999",
        ),
        rx.divider(
            border_color="black", width="100%", height="1em", border_bottom="2px solid"
        ),
        rx.foreach(DashBoardPageState.closed_bugs, project_display_new_bug),
    )
