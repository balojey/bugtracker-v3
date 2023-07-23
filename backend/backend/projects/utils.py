from pprint import pprint
from datetime import datetime
from beanie.odm.fields import Link
from ..models import Project, ProjectMember, User, Bug, Comment, File
from ..roles import Role, ProjectMemberRole
from .schemas import ProjectIn, ProjectOut, ProjectUpdate


async def write_project(creator, project: ProjectIn) -> Project:
    """A function to write a project to the database"""
    try:
        project = await Project(created_by=creator, **project.dict()).insert()
        project = await Project.get(project.id, fetch_links=True)
        project_member = await ProjectMember(
            user=creator,
            project=project,
            role_assigned_by=creator,
            role=ProjectMemberRole.ADMIN,
        ).insert()
        return project
    except Exception as e:
        raise e


async def read_project(project_id: str) -> Project:
    """A function to read a project from the database"""
    try:
        project = await Project.get(project_id, fetch_links=True)
        if not project:
            raise Exception("Project not found")
        return project
    except Exception as e:
        raise Exception(e)


async def read_projects(user: User) -> list[Project]:
    """A function to read all project a user is a member of from the database"""
    try:
        # Get all project members objects that belongs to user
        pms = await ProjectMember.find().to_list()
        pms = [pm for pm in pms if pm.user.ref.id == user.id]
        if not pms:
            raise Exception("No project found")

        # Get the projects of each project member
        projects = [await Project.get(pm.project.ref.id) for pm in pms]

        # Fetch all relationships
        for project in projects:
            await project.fetch_all_links()
        return projects
    except Exception as e:
        raise Exception(e)


async def edit_project(db_project: Project, project: ProjectUpdate) -> ProjectOut:
    """A function to update a project from the database"""
    try:
        db_project.name = project.name
        db_project.description = project.description
        db_project.updated_at = datetime.utcnow()
        await db_project.save()
        return await read_project(db_project.id)
    except Exception as e:
        raise e


async def remove_project(project: Project) -> None:
    """A function to remove a project from the database"""
    try:
        # Get project members of project
        project_members = await ProjectMember.all().to_list()
        pms = []
        for pm in project_members:
            if pm.project.ref.id == project.id:
                pms.append(pm)

        # Get bugs of project, files of bugs and comments of bugs
        bugs = await Bug.all().to_list()
        if bugs:
            bgs = []
            fls = []
            cmnts = []
            for bg in bugs:
                if bg.project.ref.id == project.id:
                    bgs.append(bg)
                    files = await File.all().to_list()
                    if files:
                        for fl in files:
                            if fl.bug.ref.id == bg.id:
                                fls.append(fl)
                    comments = await Comment.all().to_list()
                    if comments:
                        for cmnt in comments:
                            if cmnt.bug.ref.id == bg.id:
                                cmnts.append(cmnt)
            # Delete bugs
            if bgs:
                deleted_bgs = [await bg.delete() for bg in bgs]
            # Delete files
            if fls:
                deleted_fls = [await fl.delete() for fl in fls]
            # Delete comments
            if cmnts:
                deleted_cmnts = [await cmnt.delete() for cmnt in cmnts]

        # Delete project members
        deleted_pms = [await pm.delete() for pm in pms]
        # Delete project
        await project.delete()
    except Exception as e:
        raise e
