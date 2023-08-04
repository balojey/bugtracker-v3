from enum import Enum


class Priority(str, Enum):
    """Priority enumeration."""

    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    NONE = "NONE"
