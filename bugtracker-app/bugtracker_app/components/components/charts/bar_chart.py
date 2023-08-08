import reflex as rx


def bar_chart(*children, x: list, y: list) -> rx.Component:
    """Make bar chart"""

    return rx.box(
        rx.chart(
            rx.bar(
                data=rx.data(
                    "bar",
                    x=x,
                    y=y,
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
        *children,
    )
