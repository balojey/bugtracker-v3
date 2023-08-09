import reflex as rx


def view_member(member, **props):
    """View member"""

    return rx.text(member.full_name)
