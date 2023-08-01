from enum import Enum


class Role(str, Enum):
    """User roles"""

    DEVELOPER = "developer"
    PROJECT_MANAGER = "project_manager"
    QA_TESTER = "qa_tester"
    OTHER = "other"


class ProjectMemberRole(str, Enum):
    """ProjectMember roles"""

    DEVELOPER = "developer"
    PROJECT_MANAGER = "project_manager"
    QA_TESTER = "qa_tester"
    ADMIN = "admin"


roles: list[Role] = [Role.DEVELOPER, Role.PROJECT_MANAGER, Role.QA_TESTER]
