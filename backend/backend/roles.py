from enum import Enum


class Role(str, Enum):
    """User roles"""

    DEVELOPER = "developer"
    PROJECT_MANAGER = "project_manager"
    QA_TESTER = "qa_tester"
    ADMIN = "admin"
