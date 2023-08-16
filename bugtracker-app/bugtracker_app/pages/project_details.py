import reflex as rx
from ..components.components import (
    base_layout,
    project_details_heading,
    assigned_members,
    ticket_list,
)


def project_details():
    """Project details page"""

    return base_layout(
        rx.box(
            project_details_heading(margin_bottom="3em"),
            rx.box(
                assigned_members(width="10%"),
                ticket_list(width="10%"),
                display="grid",
                grid_template_columns="auto auto",
                gap="3em",
            ),
            width="100%",
            padding="3em",
        )
    )
