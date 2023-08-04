import reflex as rx
from ..states.sidebar_state import SideBarState, display_project_name
from ..states.state import State


def sidebar():
    """The sidebar component."""
    return rx.vstack(
        rx.vstack(
            rx.image(src="/favicon.ico", margin="0 auto"),
            rx.link(
                rx.heading(
                    "Bug Tracker",
                    text_align="center",
                    margin_bottom="1em",
                ),
                href="/",
            ),
            rx.box(
                rx.accordion(
                    rx.accordion_item(
                        rx.accordion_button(
                            rx.text("Projects", font_size="1.2em"),
                            rx.spacer(),
                            rx.accordion_icon(),
                            on_click=SideBarState.get_projects,
                        ),
                        rx.accordion_panel(
                            rx.foreach(
                                SideBarState.projects,
                                display_project_name,
                            ),
                        ),
                    ),
                    allow_multiple=True,
                    width="100%",
                ),
                width="100%",
                margin_top="50px",
            ),
            width="100%",
            padding_x="1em",
            padding_y="1em",
        ),
        rx.box(
            rx.button(
                "Logout",
                on_click=SideBarState.handle_logout_click,
                width="100%",
            ),
            position="absolute",
            bottom="5%",
            padding="0.5em",
            width="100%",
        ),
        position="fixed",
        height="100%",
        left="0px",
        top="0px",
        z_index="500",
        border_right="1px solid #eaeaea",
        width="30%",
        max_width="30%",
    )
