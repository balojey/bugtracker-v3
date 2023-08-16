import reflex as rx
from ..states import ProjectDetailsState
from ..models import Ticket, Project
from .schemas import AttachmentOut, TicketHistoryOut, CommentOut
from ..enumerations import TicketType, Priority, Status, Action
from .manage_project_users_state import Member
from ..models import User, TicketHistory


class ProjectTicketState(ProjectDetailsState):
    """Project ticket state"""

    ticket_title: str = ""
    ticket_description: str = ""
    ticket_submitter: str = ""
    ticket_assigned_developer: str = ""
    ticket_ticket_type: TicketType
    ticket_priority: Priority
    ticket_status: Status
    ticket_project: str = ""
    attachments: list[AttachmentOut]
    history: list[TicketHistoryOut]
    comments: list[CommentOut]
    ticket_created_at: str = ""
    ticket_updated_at: str = ""

    def get_ticket_details(self):
        """Get ticket"""

        if not self.logged_in:
            return rx.redirect("/login")

        with rx.session() as session:
            ticket = session.query(Ticket).get(self.ticket_id)
            self.ticket_title = ticket.title
            self.ticket_description = ticket.description
            self.ticket_priority = ticket.priority
            self.ticket_ticket_type = ticket.ticket_type
            self.ticket_status = ticket.status
            self.ticket_assigned_developer = (
                session.query(User).get(ticket.assigned_developer_id).full_name
            )
            self.ticket_submitter = (
                session.query(User).get(ticket.submitter_id).full_name
            )
            self.attachments = ticket.attachments
            self.history = ticket.history
            comments = ticket.comments
            for comment in comments:
                comment.commenter = (
                    session.query(User).where(User.id == comment.commenter_id).first()
                )
            self.comments = comments
            self.ticket_created_at = ticket.created_at
            self.ticket_project = session.query(Project).get(ticket.project_id).title
            if ticket.created_at != ticket.updated_at:
                self.ticket_updated_at = ticket.updated_at

    @rx.var
    def get_history(self) -> list[TicketHistoryOut]:
        """Get ticket history"""

        with rx.session() as session:
            history = (
                session.query(TicketHistory)
                .where(TicketHistory.ticket_id == self.ticket_id)
                .all()
            )
            for item in history:
                if item.action == Action.ASSIGNED_DEVELOPER_CHANGE:
                    if item.previous_value:
                        item.previous_value = (
                            session.query(User).get(item.previous_value).full_name
                        )
                    if item.present_value:
                        item.present_value = (
                            session.query(User).get(item.present_value).full_name
                        )
        return history
