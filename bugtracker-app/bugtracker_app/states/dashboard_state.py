from .base import State
from ..enumerations import Priority, Status, TicketType
from ..models import Ticket, User
import reflex as rx


class DashBoardState(State):
    """Dashboard state"""

    priorities: list = [Priority.HIGH, Priority.LOW, Priority.MEDIUM, Priority.NONE]
    priorities_values: list = []

    ticket_types: list = [
        TicketType.BUG_ERROR,
        TicketType.FEATURE_REQUEST,
        TicketType.CHANGE_REQUEST,
        TicketType.DOCUMENTATION,
        TicketType.OTHER,
        TicketType.FEEDBACK,
        TicketType.SUPPORT_HELPDESK,
        TicketType.INCIDENT,
        TicketType.TASK,
        TicketType.SECURITY,
    ]
    ticket_types_values: list = []

    ticket_statuses: list = [
        Status.OPEN,
        Status.IN_PROGRESS,
        Status.RESOLVED,
        Status.REOPENED,
        Status.CLOSED,
        Status.DUPLICATE,
        Status.PENDING,
    ]
    ticket_statuses_values: list = []

    ticket_submitters: list = []
    ticket_submitters_values: list = []

    def get_ticket_priority_params(self):
        """Get ticket priority parameters"""

        for priority in self.priorities:
            with rx.session() as session:
                self.priorities_values.append(
                    session.query(Ticket).where(Ticket.priority == priority).count()
                )

    def get_ticket_type_params(self):
        """Get ticket type parameters"""

        for ticket_type in self.ticket_types:
            with rx.session() as session:
                self.ticket_types_values.append(
                    session.query(Ticket)
                    .where(Ticket.ticket_type == ticket_type)
                    .count()
                )

    def get_ticket_status_params(self):
        """Get ticket status parameters"""

        for ticket_status in self.ticket_statuses:
            with rx.session() as session:
                self.ticket_statuses_values.append(
                    session.query(Ticket).where(Ticket.status == ticket_status).count()
                )

    def get_ticket_submitter_params(self):
        """Get ticket submitter parameters"""

        with rx.session() as session:
            submitters_ids = session.query(Ticket.submitter_id).all()
            submitters_ids = list(set(submitters_ids))
            for submitter_id in submitters_ids:
                self.ticket_submitters.append(
                    session.query(User).where(User.id == submitter_id[0]).first().name
                )
                self.ticket_submitters_values.append(
                    session.query(Ticket)
                    .where(Ticket.submitter_id == submitter_id[0])
                    .count()
                )

    def prepare_dashboard(self):
        """Prepare dashboard for view"""

        self.ticket_types = []
        self.ticket_types_values = []
        self.ticket_statuses = []
        self.ticket_statuses_values = []
        self.ticket_submitters = []
        self.ticket_submitters_values = []
        self.priorities = []
        self.priorities_values = []

        self.check_login()
        self.get_ticket_priority_params()
        self.get_ticket_type_params()
        self.get_ticket_status_params()
        self.get_ticket_submitter_params()
        print("Priorities: ", self.priorities)
        print("Priorities_values", self.priorities_values)
        print("Ticket_types: ", self.ticket_types)
        print("Ticket_types_values: ", self.ticket_types_values)
        print("Ticket_statuses: ", self.ticket_statuses)
        print("Ticket_statuses_values: ", self.ticket_statuses_values)
        print("Ticket_submitters: ", self.ticket_submitters)
        print("Ticket_submitters_values: ", self.ticket_submitters_values)
