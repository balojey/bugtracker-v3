from ...states import DashBoardState
from ...enumerations import Priority, TicketType, Status
import reflex as rx
from .charts import bar_chart, pie_chart


def dashboard_charts(**props) -> rx.Component:
    """Make all dashboard charts"""

    return rx.box(
        bar_chart(
            rx.text("Tickets by Priority"),
            x=[Priority.HIGH, Priority.LOW, Priority.MEDIUM, Priority.NONE],
            y=[2, 5, 3, 8],
        ),
        pie_chart(
            rx.text("Tickets by types"),
            x=[
                TicketType.BUG_ERROR,
                TicketType.FEATURE_REQUEST,
                TicketType.CHANGE_REQUEST,
                TicketType.DOCUMENTATION,
                TicketType.OTHER,
                TicketType.FEEDBACK,
                TicketType.SUPPORT_HELPDESK,
                TicketType.INCIDENT,
                TicketType.TASK,
                TicketType.SECURITY,
            ],
            y=[1, 2, 3, 10, 4, 5, 8, 3, 2, 6],
        ),
        pie_chart(
            rx.text("Tickets by Submitter"),
            x=[
                Status.OPEN,
                Status.IN_PROGRESS,
                Status.RESOLVED,
                Status.REOPENED,
                Status.CLOSED,
                Status.DUPLICATE,
                Status.PENDING,
            ],
            y=[1, 2, 3, 4, 10, 4, 5],
        ),
        bar_chart(
            rx.text("Tickets by Status"),
            x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"],
            y=[1, 2, 3, 10, 4],
        ),
        display="grid",
        gap="3em",
        grid_template_columns="1fr 1fr",
        align_items="center",
        justify_items="center",
        **props,
    )
