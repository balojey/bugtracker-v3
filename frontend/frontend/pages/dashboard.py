import reflex as rx
from ..states.dashboard_state import DashBoardPageState
from ..components.sidebar import sidebar
from ..components.project_overview import project_overview
from ..components.project_bugs import project_bugs
from ..components.dashboard_form import dashboard_form
from ..components.project_members import project_members
from ..components.dashboard_intro import dashboard_intro


def dashboard():
    """The dashboard page"""
    return rx.cond(
        DashBoardPageState.is_authenticated,
        rx.box(
            rx.flex(
                sidebar(),
                rx.vstack(
                    rx.cond(
                        DashBoardPageState.project_in_view_id,
                        rx.box(
                            project_overview(),
                            dashboard_form(),
                            project_bugs(),
                            project_members(),
                            width="100%",
                        ),
                        rx.box(dashboard_intro()),
                    ),
                    width="70%",
                    max_width="70%",
                    margin_left="auto",
                    padding="1em",
                ),
            ),
            padding="0px",
            margin="0px",
            width="100%",
        ),
        rx.box(
            rx.box(
                rx.heading("Please login to continue", size="sm"),
                rx.link(
                    "Login",
                    href="/login",
                    as_="button",
                    color="white",
                    bg="blue",
                    padding="1em",
                    margin="1em",
                    on_click=rx.redirect("/login"),
                ),
                padding="3em",
                margin="1em",
                border="1px solid #eaeaea",
            ),
            display="flex",
            justify_content="center",
            align_items="center",
            flex_direction="column",
            min_height="100vh",
            min_width="100%",
        ),
    )
