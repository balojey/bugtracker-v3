from enum import Enum


class BugStatus(int, Enum):
    """Bug status enum"""
    NEW = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    CLOSED = 4