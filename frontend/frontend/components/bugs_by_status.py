import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from .project_display_bug import project_display_new_bug


def new_bugs():
    """New bugs"""
    return rx.vstack(
        rx.heading("New", size="md"),
        rx.hstack(
            rx.text(DashBoardPageState.new_bugs_count),
            rx.text("bugs available"),
        ),
        rx.divider(border_color="black", width="100%"),
        rx.foreach(DashBoardPageState.new_bugs, project_display_new_bug),
    )


def in_progress_bugs():
    """New bugs"""
    return rx.vstack(
        rx.heading("In Progress", size="md"),
        rx.hstack(
            rx.text(DashBoardPageState.in_progress_bugs_count),
            rx.text("bugs available"),
        ),
        rx.divider(border_color="black", width="100%"),
        rx.foreach(DashBoardPageState.in_progress_bugs, project_display_new_bug),
    )


def resolved_bugs():
    """New bugs"""
    return rx.vstack(
        rx.heading("Resolved", size="md"),
        rx.hstack(
            rx.text(DashBoardPageState.resolved_bugs_count),
            rx.text("bugs available"),
        ),
        rx.divider(border_color="black", width="100%"),
        rx.foreach(DashBoardPageState.resolved_bugs, project_display_new_bug),
    )


def closed_bugs():
    """New bugs"""
    return rx.vstack(
        rx.heading("Closed", size="md"),
        rx.hstack(
            rx.text(DashBoardPageState.closed_bugs_count),
            rx.text("bugs available"),
        ),
        rx.divider(border_color="black", width="100%"),
        rx.foreach(DashBoardPageState.closed_bugs, project_display_new_bug),
    )
