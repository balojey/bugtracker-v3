from datetime import datetime
from ..projects.utils import read_project
from ..models import ProjectMember, Project, User
from ..roles import ProjectMemberRole
from .schemas import ProjectMemberIn, ProjectMemberOut, ProjectMemberUpdate


async def check_user_presence_in_project(user: User, project: Project) -> bool:
    """A function to check the presence of a user in a project"""
    pms = await ProjectMember.all().to_list()
    for pm in pms:
        if pm.user.ref.id == user.id and pm.project.ref.id == project.id:
            return True
    return False


async def write_project_member(
    admin: User, project: Project, project_member: ProjectMemberIn
) -> ProjectMember:
    """A function to write a project_member to the database"""
    try:
        # Get member with email
        member = await User.find_one(User.email == project_member.email)

        # Check if member already exist as a project member in project
        if await check_user_presence_in_project(member, project):
            raise Exception("Already a member")

        # Create project member
        project_member = await ProjectMember(
            user=member,
            project=project,
            role_assigned_by=admin,
            **project_member.dict()
        ).insert()
        # Get db project_member
        return await read_project_member(project_member.id)
    except Exception as e:
        raise e


async def read_project_member(project_member_id: str) -> ProjectMember:
    """A function to read a project_member from the database"""
    try:
        project_member = await ProjectMember.get(project_member_id, fetch_links=True)
        if not project_member:
            raise Exception("ProjectMember not found")
        return project_member
    except Exception as e:
        raise e


# # delete
# async def read_project_members(project: Project) -> list:
#     """A function to read project_members from the database"""
#     try:
#         return project.project_members
#     except Exception as e:
#         raise e


async def edit_project_member_role(
    admin: User, project_member: ProjectMember, member_role: ProjectMemberUpdate
) -> ProjectMember:
    """A function to update a project_member from the database"""
    try:
        if project_member.project.created_by.id == project_member.user.id:
            raise Exception("Cannot edit project owner")
        project_member.role = member_role.role
        project_member.role_assigned_by = admin
        project_member.updated_at = datetime.utcnow()
        await project_member.save()
        return await read_project_member(project_member.id)
    except Exception as e:
        raise e


async def remove_project_member(project_member: ProjectMember) -> None:
    """A function to remove a project_member from the database"""
    try:
        await project_member.delete()
    except Exception as e:
        raise e


async def fetch_project_members(project: Project) -> list[ProjectMember]:
    """A function to fetch project members from the database"""
    try:
        project_members = await ProjectMember.all().to_list()
        pms = [pm for pm in project_members if pm.project.ref.id == project.id]
        for pm in pms:
            await pm.fetch_all_links()
        return pms
    except Exception as e:
        raise e


async def fetch_project_member(user: User, project: Project) -> ProjectMember:
    """Fetch project member"""
    pms = [
        pm
        for pm in await ProjectMember.find().to_list()
        if pm.project.ref.id == project.id
        and (
            user.id == pm.user.ref.id
            and (
                pm.role == ProjectMemberRole.ADMIN
                or pm.role == ProjectMemberRole.PROJECT_MANAGER
            )
        )
    ]
    if not pms:
        raise Exception("You are neither a manager nor an admin")
    return pms[0]


async def fetch_project_member_by_user(user: User, project: Project) -> ProjectMember:
    """Fetch project member"""
    pms = [
        pm
        for pm in await ProjectMember.find().to_list()
        if pm.project.ref.id == project.id and user.id == pm.user.ref.id
    ]
    if not pms:
        raise Exception("You are not a member of this project")
    return pms[0]
