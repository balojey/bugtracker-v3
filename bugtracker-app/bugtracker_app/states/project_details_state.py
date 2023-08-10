import reflex as rx
from .my_projects_state import MyProjectState
from ..models import Project, Ticket, User
from .manage_project_users_state import Member
from ..enumerations import TicketType, Priority, Status


class TicketOut(rx.Base):
    """Ticket out."""

    title: str
    submitter: Member
    assigned_developer: Member
    ticket_type: TicketType
    priority: Priority
    status: Status
    created_at: str


class ProjectDetailsState(MyProjectState):
    """State for project details page."""

    title: str = ""
    description: str = ""
    members: list[User] = []

    def get_project_details(self) -> Project:
        """Project."""
        if not self.logged_in:
            return rx.redirect("/login")
        with rx.session() as session:
            project = session.query(Project).get(self.project_id)
            self.title = project.title
            self.description = project.description
            self.members = project.members

    @rx.var
    def tickets(self) -> list[TicketOut]:
        """List of tickets."""
        with rx.session() as session:
            tickets = session.query(Ticket).filter_by(project_id=self.project_id).all()
            for ticket in tickets:
                ticket.submitter = session.query(User).get(ticket.submitter_id)
                ticket.assigned_developer = session.query(User).get(
                    ticket.assigned_developer_id
                )
            return tickets
