from pprint import pprint
from beanie.odm.fields import Link
from models import Project, User, ProjectMember, Bug, Comment
from projects.utils import read_project
from projects.schemas import ProjectOut
from project_members.utils import fetch_project_member, fetch_project_member_by_user
from roles import ProjectMemberRole


async def check_project_permission(user: User, project: Project) -> bool:
    """A function to check if a user is a project's admin"""
    try:
        isMember = False
        project_members = await ProjectMember.all().to_list()
        for pm in project_members:
            if pm.user.ref.id == user.id and pm.project.ref.id == project.id:
                isMember = not isMember
                break
        if not isMember:
            raise Exception("You are not a member of this project")
        if pm.role != ProjectMemberRole.ADMIN:
            raise Exception("Not enough permission")
        return True
    except Exception as e:
        raise e


async def check_user_presence_in_project(user: User, project: Project) -> bool:
    """A function to check the presence of a user in a project"""
    pms = await ProjectMember.all().to_list()
    for pm in pms:
        if pm.user.ref.id == user.id and pm.project.ref.id == project.id:
            return True
    raise Exception("You are not a member of this project")


# async def check_project_member_permission(user: User, project_member: ProjectMember) -> bool:
#     """A function to check if a user has permission to access a project"""
#     try:

#     except Exception as e:
#         raise e


# async def check_project_member_permission_for_bug(user, project_id: str) -> bool:
#     """A function to check if a user is a member of a project"""
#     try:
#         project = await read_project(project_id)
#         project_members = [
#             project_member.to_dict() for project_member in project.project_members
#         ]
#         project_members = [
#             await read_project_member(project_member["id"])
#             for project_member in project_members
#         ]
#         for project_member in project_members:
#             if str(user.id) == str(project_member.user.to_dict()["id"]):
#                 return True
#         raise Exception("You are not a member of this project")
#     except Exception as e:
#         raise e


async def check_bug_assignment_permission_for_user(
    user: User, project: Project
) -> bool:
    """A function to check if a user is a project manager or admin of a project"""
    try:
        if await fetch_project_member(user, project):
            return True
        raise Exception("You are not a project manager or an admin of this project")
    except Exception as e:
        raise e


async def check_reporter(user: User, reporter: ProjectMember) -> bool:
    """A function to verify if user is reporter"""
    if user.id == reporter.user.id:
        return True
    raise Exception("You cannot edit this bug")


async def check_author_or_admin(user: User, comment: Comment) -> bool:
    """A function to verify if user is reporter"""
    pm = await fetch_project_member_by_user(user, comment.bug.project)
    if user.id == comment.author.user.id or pm.role == ProjectMemberRole.ADMIN:
        return True
    raise Exception("You cannot edit this bug")


async def check_assigned_developer(
    user: User, assigned_developer: ProjectMember
) -> bool:
    """A function to verify if user is assigned_developer"""
    if user.id == assigned_developer.user.id:
        return True
    raise Exception("You cannot edit this bug")


async def check_reporter_and_assigned_developer(
    user: User, reporter: ProjectMember, assigned_developer: ProjectMember
) -> bool:
    """A function to verify if user is assigned_developer"""
    if user.id == assigned_developer.user.id or user.id == reporter.user.id:
        return True
    raise Exception("You cannot edit this bug")


async def check_bug_delete_permission(user: User, bug: Bug) -> bool:
    """A function that checks if user is the reporter of bug or
    the admin of the project and if assigned developer exists

    return True: if assigned developer is pm
                 if bug reporter is pm
                 if pm role is admin

    raise Exception: if assigned developer exists and pm is reporter
    """
    pms = await ProjectMember.all().to_list()
    pm = [pm for pm in pms if pm.user.ref.id == user.id]
    if not pm:
        raise Exception("You are neither a manager nor an admin")
    pm = pm[0]
    if bug.assigned_developer and pm.id == bug.reporter.id:
        if bug.assigned_developer.id != pm.id:
            raise Exception(
                "You cannot delete this bug because a developer has been assigned to this bug"
            )
        return True
    if (
        pm.id == bug.reporter.id
        or pm.role == ProjectMemberRole.ADMIN
        or (bug.assigned_developer and pm.id == bug.assigned_developer.id)
    ):
        return True
    raise Exception("You cannot delete this bug")
