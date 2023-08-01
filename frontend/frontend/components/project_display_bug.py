import reflex as rx
from ..states.dashboard_state import DashBoardPageState


def project_display_new_bug(project: dict):
    """Display project bug"""
    p = f"{project['reporter']}, {project['description']}"
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.vstack(
            rx.heading(project["title"], size="sm"),
            rx.text(project["reporter"]),
            rx.text(project["updated_at"]),
            rx.text(project["description"]),
        ),
    )
