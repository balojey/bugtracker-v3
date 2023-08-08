from ...states import DashBoardState
from ...enumerations import Priority, TicketType, Status
import reflex as rx


def dashboard_charts(**props) -> rx.Component:
    """Make all dashboard charts"""

    return rx.box(
        rx.box(
            rx.chart(
                rx.bar(
                    data=rx.data(
                        "bar",
                        x=[Priority.HIGH, Priority.LOW, Priority.MEDIUM, Priority.NONE],
                        y=[2, 5, 3, 8],
                    ),
                    style={
                        "data": {
                            "fill": "rgb(107,99,246)",
                            "stroke": "black",
                            "strokeWidth": 2,
                        }
                    },
                ),
                domain_padding={"x": 20, "y": 0},
            ),
            rx.text("Tickets by priority"),
        ),
        rx.box(
            rx.pie(
                data=rx.data(
                    "pie",
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
                color_scale="qualitative",
                pad_angle=5.0,
                inner_radius=100.0,
                start_angle=90.0,
            ),
            rx.text("Tickets by types"),
        ),
        rx.box(
            rx.pie(
                data=rx.data(
                    "pie",
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
                color_scale="qualitative",
                pad_angle=5.0,
                inner_radius=100.0,
                start_angle=90.0,
            ),
            rx.text("Tickets by submitter"),
        ),
        rx.box(
            rx.chart(
                rx.bar(
                    data=rx.data(
                        "bar",
                        x=["Cats", "Dogs", "Birds", "Fish", "Reptiles"],
                        y=[1, 2, 3, 10, 4],
                    ),
                    style={
                        "data": {
                            "fill": "rgb(107,99,246)",
                            "stroke": "black",
                            "strokeWidth": 2,
                        }
                    },
                ),
                domain_padding={"x": 20, "y": 0},
            ),
            rx.text("Tickets by status"),
        ),
        display="grid",
        gap="3em",
        grid_template_columns="1fr 1fr",
        align_items="center",
        justify_items="center",
        **props,
    )
