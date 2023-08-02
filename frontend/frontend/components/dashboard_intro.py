import reflex as rx
from ..states.dashboard_state import DashBoardPageState


def dashboard_intro() -> rx.Component:
    """Dashboard intro"""
    return rx.vstack(
        rx.heading(
            "Welcome to the dashboard",
            size="lg",
            margin_top="16px",
            margin_bottom="16px",
        ),
        rx.button(
            rx.icon(tag="add"),
            "   Create a new project",
            on_click=DashBoardPageState.change_create_project_state,
            padding="1em",
        ),
        rx.modal(
            rx.modal_overlay(
                rx.modal_content(
                    rx.flex(
                        rx.spacer(),
                        rx.button(
                            rx.icon(tag="close"),
                            on_click=DashBoardPageState.change_create_project_state,
                            border_radius="100%",
                        ),
                    ),
                    rx.modal_header("Create Project"),
                    rx.modal_body(
                        rx.vstack(
                            rx.form(
                                rx.vstack(
                                    rx.input(
                                        placeholder="Project Name",
                                        id="name",
                                        is_required=True,
                                        size="lg",
                                    ),
                                    rx.text_area(
                                        placeholder="Project description",
                                        id="description",
                                        is_required=True,
                                        size="lg",
                                    ),
                                    rx.button("Create", type_="submit"),
                                ),
                                on_submit=DashBoardPageState.handle_project_form_submit,
                            ),
                        )
                    ),
                    padding="2em",
                )
            ),
            is_open=DashBoardPageState.create_project_state,
        ),
    )
