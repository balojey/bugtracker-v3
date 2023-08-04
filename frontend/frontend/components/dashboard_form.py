import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from ..schemas.roles import roles
from ..schemas.priority import Priority, priorities

color = "rgb(107,99,246)"


def dashboard_form():
    """Form for reporting new bug and form for adding project members"""
    return rx.hstack(
        rx.box(
            rx.button(
                rx.icon(tag="add"),
                " ",
                "Report a Bug",
                on_click=DashBoardPageState.set_report_a_bug,
            ),
            rx.modal(
                rx.modal_overlay(
                    rx.modal_content(
                        rx.modal_header("Report a bug"),
                        rx.modal_body(
                            rx.form(
                                rx.vstack(
                                    rx.input(
                                        placeholder="Bug title",
                                        id="title",
                                        is_required=True,
                                        size="lg",
                                    ),
                                    rx.text_area(
                                        placeholder="Bug description",
                                        id="description",
                                        is_required=True,
                                        size="lg",
                                    ),
                                    rx.text_area(
                                        placeholder="Steps to reproduce",
                                        id="steps_to_reproduce",
                                        is_required=True,
                                        size="lg",
                                    ),
                                    rx.hstack(
                                        rx.select(
                                            priorities,
                                            placeholder="Select priority",
                                            on_change=DashBoardPageState.set_priority,
                                        ),
                                        rx.hstack(
                                            rx.upload(
                                                rx.hstack(
                                                    rx.button(
                                                        "Select File",
                                                        color=color,
                                                        bg="white",
                                                        border_radius="none",
                                                    ),
                                                ),
                                                border=f"1px solid {color}",
                                                padding="0.1em",
                                            ),
                                            rx.button(
                                                "Upload",
                                                on_click=lambda: DashBoardPageState.handle_upload(
                                                    rx.upload_files()
                                                ),
                                            ),
                                        ),
                                    ),
                                    rx.vstack(
                                        rx.foreach(
                                            DashBoardPageState.img,
                                            lambda img: rx.image(src=img),
                                        ),
                                    ),
                                    rx.button(
                                        "Report",
                                        type_="submit",
                                    ),
                                ),
                                on_submit=DashBoardPageState.handle_report_bug_form_data_submit,
                            ),
                        ),
                        rx.modal_footer(
                            rx.button(
                                "Close",
                                on_click=DashBoardPageState.set_report_a_bug,
                            )
                        ),
                    )
                ),
                is_open=DashBoardPageState.report_a_bug,
            ),
        ),
        rx.spacer(),
        rx.box(
            rx.cond(
                DashBoardPageState.is_admin,
                rx.form(
                    rx.hstack(
                        rx.input(
                            placeholder="User Email",
                            id="email",
                            type_="email",
                        ),
                        rx.select(
                            roles,
                            placeholder="Select a role (default: Developer)",
                            on_change=DashBoardPageState.set_role,
                        ),
                        rx.button("Submit", type_="submit", padding="1.5em"),
                    ),
                    on_submit=DashBoardPageState.handle_add_project_member_submit,
                ),
            ),
        ),
    )