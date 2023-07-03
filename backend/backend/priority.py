from enum import Enum


class Priority(Enum):
    """Enum for priority of a task"""

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4
    IMMEDIATE = 5
    CRITICAL = 6
    BLOCKER = 7

    def __str__(self):
        return self.name
