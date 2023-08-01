import reflex as rx
from ..states.sidebar_state import SideBarState, display_project_name
from ..states.state import State


def sidebar():
    """The sidebar component."""
    return rx.box(
        rx.vstack(
            rx.image(src="/favicon.ico", margin="0 auto"),
            rx.heading(
                "Bug Tracker",
                text_align="center",
                margin_bottom="1em",
            ),
            width="250px",
            padding_x="1em",
            padding_y="1em",
        ),
        rx.box(
            rx.flex(
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
                    overflow="visible",
                ),
                rx.box(
                    rx.button(
                        rx.icon(tag="add"),
                        on_click=SideBarState.change_create_project_state,
                        background="transparent",
                        border="none",
                    ),
                    rx.modal(
                        rx.modal_overlay(
                            rx.modal_content(
                                rx.vstack(
                                    rx.cond(
                                        SideBarState.status,
                                        rx.alert(
                                            rx.alert_icon(),
                                            rx.alert_title(SideBarState.message),
                                            status=SideBarState.status,
                                        ),
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
                                            on_submit=SideBarState.handle_project_form_submit,
                                        ),
                                        rx.divider(),
                                        rx.heading("Results"),
                                        rx.text(
                                            SideBarState.project_form_data.to_string()
                                        ),
                                    )
                                ),
                                rx.modal_footer(
                                    rx.button(
                                        "Close",
                                        on_click=SideBarState.change_create_project_state,
                                    )
                                ),
                            )
                        ),
                        is_open=SideBarState.create_project_state,
                    ),
                ),
            ),
            rx.link(
                "Reports",
                href="/dashboard",
                padding="1em",
                font_size="1.2em",
            ),
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
        max_width="20%",
    )
