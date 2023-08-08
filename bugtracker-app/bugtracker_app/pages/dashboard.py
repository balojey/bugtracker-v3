import reflex as rx
from ..components.components import sidebar, header, dashboard_charts


styles = {
    "grid_container": {
        "display": "grid",
        "gap": "4em 0",
        "grid_template_columns": "20% auto",
        "max_height": "100vh",
        "min_height": "100vh",
        "max_width": "100%",
    },
    "grid_item": {},
    "header": {"grid_column": "2 / 3"},
    "sidebar": {"grid_row": "1 / 3"},
}


def dashboard():
    """Dashboard page"""
    return rx.box(
        header(style=[styles["grid_item"], styles["header"]]),
        sidebar(style=[styles["grid_item"], styles["sidebar"]]),
        dashboard_charts(style=styles["grid_item"]),
        style=styles["grid_container"],
    )
