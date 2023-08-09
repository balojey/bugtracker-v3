import reflex as rx
from ..components.components import base_layout, view_and_remove_members


def manage_project_users():
    """Manage project users"""

    return base_layout(rx.box(view_and_remove_members()))
