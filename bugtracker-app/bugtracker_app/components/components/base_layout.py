import reflex as rx
from . import sidebar, header


styles = {
    "grid_container": {
        "display": "grid",
        "gap": "4em 0",
        "grid_template_columns": "20% auto",
        "grid_template_rows": "auto 1fr",
        "max_height": "100vh",
        "min_height": "100vh",
        "max_width": "100%",
    },
    "grid_item": {},
    "header": {"grid_column": "2 / 3"},
    "sidebar": {"grid_row": "1 / 3"},
}


def base_layout(*children):
    """Dashboard page"""
    return rx.box(
        header(style=[styles["grid_item"], styles["header"]]),
        sidebar(style=[styles["grid_item"], styles["sidebar"]]),
        *children,
        style=styles["grid_container"],
    )
