import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from ..schemas.priority import Priority, priorities

color = "rgb(107,99,246)"


def project_display_new_bug(bug: dict):
    """Display project bug"""
    return rx.cond(
        DashBoardPageState.project_in_view_id,
        rx.box(
            rx.heading(
                bug["title"],
                size="sm",
                text_align="left",
                _hover={"color": "#000000"},
            ),
            rx.text(
                bug["reporter"],
                ", ",
                bug["updated_at"],
                text_align="left",
                font_size="0.8em",
                color="#999999",
                padding_top="0.3em",
                _hover={"color": "#999999"},
            ),
            rx.text(
                bug["description"],
                text_align="left",
                padding_y="0.7em",
                _hover={"color": "#000000"},
            ),
            rx.tooltip(
                rx.text(
                    "",
                    background_color=bug["priority"],
                    width="1em",
                    height="1em",
                    border_radius="50%",
                    _hover={"background_color": f"{bug['priority']}"},
                ),
                label="priority",
            ),
            rx.modal(
                rx.modal_overlay(
                    rx.modal_content(
                        rx.modal_header("View bug"),
                        rx.modal_body(
                            rx.box(
                                rx.heading(
                                    "Title: ",
                                    bug["title"],
                                    size="sm",
                                ),
                                rx.text(
                                    "Reporter: ",
                                    bug["reporter"],
                                    ", ",
                                    bug["updated_at"],
                                    font_size="0.8em",
                                    color="#999999",
                                    padding_top="0.3em",
                                ),
                                rx.text(
                                    "Description: ",
                                    bug["description"],
                                    padding_y="0.7em",
                                ),
                                rx.text(
                                    "Steps to reproduce: ",
                                    bug["steps_to_reproduce"],
                                    padding_y="0.7em",
                                ),
                                rx.text(
                                    "Priority: ",
                                ),
                                rx.form(
                                    rx.select(
                                        priorities,
                                        placeholder="Select priority",
                                        on_change=DashBoardPageState.set_priority,
                                    ),
                                ),
                                rx.form(),
                                text_align="left",
                            ),
                            rx.modal_footer(
                                rx.button(
                                    "Close",
                                    on_click=DashBoardPageState.set_view_bug,
                                )
                            ),
                        ),
                    ),
                    is_open=DashBoardPageState.view_bug,
                ),
            ),
            margin="0",
            padding_y="0.7em",
            border_bottom=f"2px solid #eaeaea",
            _hover={
                "cursor": "pointer",
            },
            on_click=lambda x: DashBoardPageState.set_bug_in_view(bug["_id"]),
        ),
    )
