from enum import Enum


class Role(str, Enum):
    """Role enumeration."""

    ADMIN = "ADMIN"
    DEVELOPER = "DEVELOPER"
    PROJECT_MANAGER = "PROJECT MANAGER"
    SUBMITTER = "SUBMITTER"
