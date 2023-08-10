import reflex as rx
from ...states import ManageProjectUsersState


def view_member(member, **props):
    """View member"""

    return rx.hstack(
        rx.text(member.email),
        rx.text(member.role),
        rx.button(
            rx.icon(tag="delete"),
            on_click=lambda: ManageProjectUsersState.handle_remove_user(member.id),
        ),
        justify="space-between",
        align_items="center",
    )
