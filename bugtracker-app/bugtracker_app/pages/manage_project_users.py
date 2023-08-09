import reflex as rx
from ..components.components import (
    base_layout,
    view_and_remove_members,
    add_members_to_projects,
)


def manage_project_users():
    """Manage project users"""

    return base_layout(
        rx.box(
            view_and_remove_members(),
            add_members_to_projects(),
            width="100%",
            display="grid",
            grid_template_columns="1fr 1fr",
            grid_gap="1em",
            justify_items="center",
            align_items="center",
        )
    )
