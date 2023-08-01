from enum import Enum


class Priority(int, Enum):
    """Enum for priority of a task"""

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4
    IMMEDIATE = 5
    CRITICAL = 6
    BLOCKER = 7


class PriorityReversed(str, Enum):
    """Enum for priority of a task"""
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    URGENT = "URGENT"
    IMMEDIATE = "IMMEDIATE"
    CRITICAL = "CRITICAL"
    BLOCKER = "BLOCKER"


priorities: list[PriorityReversed] = [
    PriorityReversed.LOW.value,
    PriorityReversed.MEDIUM.value,
    PriorityReversed.HIGH.value,
    PriorityReversed.URGENT.value,
    PriorityReversed.IMMEDIATE.value,
    PriorityReversed.CRITICAL.value,
    PriorityReversed.BLOCKER.value,
]
