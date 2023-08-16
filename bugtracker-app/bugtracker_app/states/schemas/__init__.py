import reflex as rx
from ...enumerations import Action
from ..manage_project_users_state import Member


class AttachmentOut(rx.Base):
    """Attachment out"""

    file_name: str
    description: str
    file_path: str


class TicketHistoryOut(rx.Base):
    """Ticket history out"""

    action: Action
    previous_value: str
    present_value: str
    created_at: str


class CommentOut(rx.Base):
    """Comment out"""

    content: str
    commenter: Member
    created_at: str
