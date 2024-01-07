from pprint import pprint
from datetime import datetime
from beanie.odm.fields import Link
from models import Bug, Comment, Project, User, File, ProjectMember
from projects.utils import read_project
from status import ProjectStatus
from roles import ProjectMemberRole
from .schemas import BugIn, BugOut, BugUpdate, ChangePriority, ChangeStatus


async def fetch_project_member(user: User) -> ProjectMember:
    isFound = False
    pms = await ProjectMember.all().to_list()
    for pm in pms:
        if pm.user.ref.id == user.id:
            isFound = not isFound
            break
    if not isFound:
        raise Exception("You are not a member of this project")
    return pm


async def write_bug(user: User, project: Project, bug: BugIn) -> Bug:
    """A function to write a bug to the database"""
    try:
        project_member = await fetch_project_member(user)
        db_bug = await Bug(
            title=bug.title,
            description=bug.description,
            steps_to_reproduce=bug.steps_to_reproduce,
            priority=bug.priority,
            reporter=project_member,
            project=project,
        ).insert()
        db_bug = await read_bug(db_bug.id)
        if bug.bug_files:
            for file in bug.bug_files:
                file = await File(
                    filename=file.filename, url=file.url, bug=db_bug
                ).insert()
        project.status = ProjectStatus.IN_PROGRESS
        await project.save()
        return db_bug
    except Exception as e:
        raise e


async def read_bug(bug_id: str) -> Bug:
    """A function to read a bug from the database"""
    try:
        bug = await Bug.get(bug_id, fetch_links=True)
        if not bug:
            raise Exception("Bug not found")
        return bug
    except Exception as e:
        raise e


async def read_bugs(project: Project) -> list[Bug]:
    """A function to read bugs from the database"""
    try:
        bugs = await Bug.find().to_list()
        bgs = []
        for bg in bugs:
            if bg.project.ref.id == project.id:
                bgs.append(bg)
        for bg in bgs:
            await bg.fetch_all_links()
        return bgs
    except Exception as e:
        raise e


async def edit_bug(db_bug: Bug, bug: BugUpdate) -> Bug:
    """A function to update a bug in the database"""
    try:
        db_bug.title = bug.title
        db_bug.description = bug.description
        db_bug.steps_to_reproduce = bug.steps_to_reproduce
        db_bug.updated_at = datetime.utcnow()
        await db_bug.save()
        return await read_bug(db_bug.id)
    except Exception as e:
        raise e


async def check_developer_role_in_project(developer: ProjectMember, project: Project):
    """Check that developer has a developer role in project"""
    try:
        if (
            developer.project.id == project.id
            and developer.role == ProjectMemberRole.DEVELOPER
        ):
            return True
        raise Exception(
            "User is not a developer, change user's role before assigning them a bug"
        )
    except Exception as e:
        raise e


async def assign_bug_to_developer(
    bug: Bug, admin_or_project_manager: ProjectMember, developer: ProjectMember
) -> Bug:
    """A function to assign a bug to a developer"""
    try:
        if bug.assigned_developer and bug.assigned_developer.id == developer.id:
            raise Exception("Bug is already assigned to this developer")
        bug.assigned_developer = developer
        bug.assigner = admin_or_project_manager
        bug.updated_at = datetime.utcnow()
        await bug.save()
        return await read_bug(bug.id)
    except Exception as e:
        raise e


async def edit_bug_priority(bug: Bug, bug_priority: ChangePriority) -> Bug:
    """A function for to edit the priority of a bug"""
    try:
        bug.priority = bug_priority.priority
        bug.updated_at = datetime.utcnow()
        await bug.save()
        return await read_bug(bug.id)
    except Exception as e:
        raise e


async def edit_bug_status(bug: Bug, bug_status: ChangeStatus) -> Bug:
    """A function for to edit the priority of a bug"""
    try:
        bug.status = bug_status.status
        bug.updated_at = datetime.utcnow()
        await bug.save()
        return await read_bug(bug.id)
    except Exception as e:
        raise e


async def remove_bug(bug: Bug) -> None:
    """A function to remove a bug from the database"""
    try:
        cmnts = [
            await comment.delete()
            for comment in await Comment.find().to_list()
            if comment.bug.ref.id == bug.id
        ]
        fls = [
            await file.delete()
            for file in await File.find().to_list()
            if file.bug.ref.id == bug.id
        ]
        await bug.delete()
    except Exception as e:
        raise e
