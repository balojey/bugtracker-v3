import reflex as rx
from ..states import ProjectDetailsState
from ..models import Ticket
from .schemas import AttachmentOut, TicketHistoryOut, CommentOut
from ..enumerations import TicketType, Priority, Status
from .manage_project_users_state import Member
from pydantic import Field


class ProjectTicketState(ProjectDetailsState):
    """Project ticket state"""

    ticket_title: str = ""
    ticket_description: str = ""
    ticket_submitter: Member = Member
    ticket_assigned_developer: Member = Member
    ticket_ticket_type: TicketType
    ticket_priority: Priority
    ticket_status: Status
    attachments: list[AttachmentOut]
    history: list[TicketHistoryOut]
    comments: list[CommentOut]

    def get_ticket(self):
        """Get ticket"""

        with rx.session() as session:
            ticket = session.query(Ticket).get(self.ticket_id)
            self.ticket_title = ticket.title
