from enum import Enum


class Status(str, Enum):
    """Status enumeration."""

    OPEN = "OPEN"
    IN_PROGRESS = "IN PROGRESS"
    PENDING = "PENDING"
    RESOLVED = "RESOLVED"
    CLOSED = "CLOSED"
    REOPENED = "REOPENED"
    DUPLICATE = "DUPLICATE"
