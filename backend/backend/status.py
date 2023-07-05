from enum import Enum


class Status(Enum):
    """Enum for status of a task"""

    NEW = 1
    IN_PROGRESS = 2
    RESOLVED = 3
    CLOSED = 4

    def __str__(self):
        return self.name
    

class ProjectStatus(Enum):
    """Enum for status of a task"""

    NEW = 1
    IN_PROGRESS = 2
    CLOSED = 3

    def __str__(self):
        return self.name
