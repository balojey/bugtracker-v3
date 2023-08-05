from enum import Enum


class Role(str, Enum):
    """Role enumeration."""

    ADMIN = "ADMIN"
    ASSIGNED_ADMIN = "ASSIGNED ADMIN"
    DEVELOPER = "DEVELOPER"
    PROJECT_MANAGER = "PROJECT MANAGER"
    SUBMITTER = "SUBMITTER"
