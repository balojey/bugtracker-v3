import reflex as rx
from ..components.components import base_layout, project_row
from ..states import MyProjectState


def my_projects():
    return base_layout(
        rx.box(
            rx.button("Create a new project", width="20em", padding="1em"),
            rx.heading("My Projects"),
            rx.table(
                rx.thead(
                    rx.tr(
                        rx.th("Project Name"),
                        rx.th("Description"),
                        rx.th("Actions"),
                    )
                ),
                rx.tbody(
                    rx.foreach(MyProjectState.projects, project_row),
                ),
            ),
            width="100%",
            padding="3em",
        ),
    )
