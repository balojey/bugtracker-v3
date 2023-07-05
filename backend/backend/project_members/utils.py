from ..users.utils import find_user_by_email, find_user_by_id
from ..projects.utils import read_project
from ..models import ProjectMember
from .schemas import ProjectMemberIn, ProjectMemberOut, ProjectMemberUpdate


async def write_project_member(
    user_id: str, project_id: str, project_member: ProjectMemberIn
) -> None:
    """A function to write a project_member to the database"""
    try:
        assigned_by = await find_user_by_id(user_id)
        user = await find_user_by_email(project_member.email)
        project = await read_project(project_id)
        if not project_member.role:
            project_member.role = user.role
        project_member = await ProjectMember(
            user=user, project=project, assigned_by=assigned_by, **project_member.dict()
        ).insert()
        project_member = await ProjectMember.get(project_member.id)
        project.project_members.append(project_member)
        user.project_members.append(project_member)
        assigned_by.assigned_roles.append(project_member)
        await project.save()
        await user.save()
        await assigned_by.save()
    except Exception as e:
        raise e
    

async def read_project_member(project_member_id: str) -> ProjectMemberOut:
    """A function to read a project_member from the database"""
    try:
        print(3)
        project_member = await ProjectMember.get(project_member_id)
        print(4)
        if not project_member:
            print(5)
            raise Exception("ProjectMember not found")
        return project_member
    except Exception as e:
        print(e)
        raise e
    

async def read_project_members(project_id: str) -> list:
    """A function to read project_members from the database"""
    try:
        project = await read_project(project_id)
        if not project:
            raise Exception("Project not found")
        return project.project_members
    except Exception as e:
        raise e
    

async def edit_project_member_role(project_member_id: str, project_member: ProjectMemberUpdate) -> ProjectMemberOut:
    """A function to update a project_member from the database"""
    try:
        print(1)
        db_project_member = await read_project_member(project_member_id)
        print(2)
        db_project_member.role = project_member.role
        await db_project_member.save()
        return await read_project_member(project_member_id)
    except Exception as e:
        raise e
