from pprint import pprint
from bson import ObjectId
from beanie.odm.fields import Link
from ..models import Project, ProjectMember, User
from ..users.utils import find_user_by_id, find_user_by_project
from ..roles import Role
from .schemas import ProjectIn, ProjectOut, ProjectUpdate


async def write_project(creator_id, project: ProjectIn) -> dict:
    """A function to write a project to the database"""
    try:
        creator = await find_user_by_id(creator_id)
        project = await Project(**project.dict(), created_by=creator).insert()
        project_member = await ProjectMember(
            user=creator, project=project, role=Role.ADMIN, assigned_by=creator
        ).insert()
        project = await Project.get(project.id)
        project.project_members.append(project_member)
        creator.created_projects.append(project)
        creator.assigned_roles.append(project_member)
        creator.project_members.append(project_member)
        await creator.save()
        await project.save()
        return project
    except Exception as e:
        raise e


async def read_project(project_id: str) -> ProjectOut:
    """A function to read a project from the database"""
    try:
        project = await Project.get(project_id)
        return project
    except Exception as e:
        raise Exception(e)


async def edit_project(project_id: str, project: ProjectUpdate) -> ProjectOut:
    """A function to update a project from the database"""
    try:
        db_project = await read_project(project_id)
        db_project.name = project.name
        db_project.description = project.description
        db_project.status = project.status
        await db_project.save()
        return await read_project(project_id)
    except Exception as e:
        raise e


async def remove_project(project_id: str) -> ProjectOut:
    """A function to remove a project from the database"""
    try:
        project = await read_project(project_id)
        await project.fetch_all_links()
        creator_id: str = str(project.dict()["created_by"]["id"])
        project_members_ids: list[str] = [
            str(project_member["id"])
            for project_member in project.dict()["project_members"]
        ]
        for project_member_id in project_members_ids:
            project_member = await ProjectMember.get(project_member_id)
            await project_member.fetch_all_links()
            user_id: str = str(project_member.dict()["user"]["id"])
            assigner_id: str = str(project_member.dict()["assigned_by"]["id"])

            # Remove project_member from user
            user = await User.get(user_id)
            for pm in user.project_members:
                if str(pm.to_dict()["id"]) == project_member_id:
                    user.project_members.remove(pm)
                    break
            # Save changes
            await user.save()

            # Remove project_member from assigner
            assigner = await User.get(assigner_id)
            for ar in assigner.assigned_roles:
                if str(ar.to_dict()["id"]) == project_member_id:
                    assigner.assigned_roles.remove(ar)
                    break
            # Save changes
            await assigner.save()

            # Remove project_member from creator
            creator = await User.get(creator_id)
            for cp in creator.created_projects:
                if str(cp.to_dict()["id"]) == project_id:
                    creator.created_projects.remove(cp)
                    break
            # Save changes
            await creator.save()

            # Delete project_member
            await project_member.delete()
        await project.delete()
    except Exception as e:
        raise e


async def check_project_permission(user, project_id: str) -> bool:
    """A function to check if a user has permission to access a project"""
    try:
        if user.created_projects:
            for project_dict in user.created_projects:
                if project_dict.to_dict()["id"] == project_id:
                    break
        # if user != db_project.created_by and user not in [project_user for project_user in [user_dict.user for user_dict in db_project.project_members]]:
        #     raise HTTPException(
        #         status_code=status.HTTP_401_UNAUTHORIZED,
        #         detail="You don't have permission to update this project",
        #     )
    except Exception as e:
        # raise Exception("You don't have permission to access this project")
        raise e
