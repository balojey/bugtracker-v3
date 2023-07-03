from ..users.utils import find_user_by_email, find_user_by_id
from ..projects.utils import read_project
from ..models import ProjectMember
from .schemas import ProjectMemberIn, ProjectMemberOut, ProjectMemberUpdate


async def write_project_member(
    user_id: str, project_id: str, project_member: ProjectMemberIn
) -> ProjectMemberOut:
    """A function to write a project_member to the database"""
    try:
        assigned_by = await find_user_by_id(user_id)
        user = await find_user_by_email(project_member.email)
        project = await read_project(project_id)
        if not project_member.role:
            role = user.role
        project_member = ProjectMember(
            user=user, project=project, assigned_by=assigned_by, role=role
        ).insert()
        return project_member
    except Exception as e:
        raise e
