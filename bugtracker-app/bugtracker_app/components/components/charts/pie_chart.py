import reflex as rx


def pie_chart(*children, x: list, y: list) -> rx.Component:
    """Make bar chart"""

    return rx.box(
        rx.pie(
            data=rx.data(
                "pie",
                x=x,
                y=y,
            ),
            color_scale="qualitative",
            pad_angle=5.0,
            inner_radius=100.0,
            start_angle=90.0,
        ),
        *children,
    )
