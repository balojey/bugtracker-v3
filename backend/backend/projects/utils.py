from ..models import Project
from .schemas import ProjectIn, ProjectOut, ProjectUpdate
from ..users.utils import find_user_by_id, find_user_by_project


async def write_project(creator_id, project: ProjectIn) -> dict:
    """A function to write a project to the database"""
    creator = await find_user_by_id(creator_id)
    if not creator:
        raise Exception("User not found")
    project = await Project(**project.dict(), created_by=creator).insert()
    project = await Project.get(project.id)
    creator.created_projects.append(project)
    await creator.save()
    return project


async def read_project(project_id: str) -> ProjectOut:
    """A function to read a project from the database"""
    project = await Project.get(project_id)
    if not project:
        raise Exception("Project not found")
    # print(project)
    return project


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
        db_project = await read_project(project_id)
        user, index = await find_user_by_project(project_id)
        user.created_projects.remove(user.created_projects[index])
        await user.save()
        await db_project.delete()
        return
    except Exception as e:
        raise e


async def check_project_permission(user, project_id: str) -> bool:
    """A function to check if a user has permission to access a project"""
    is_project_found = False
    if user.created_projects:
        for project_dict in user.created_projects:
            if project_dict.to_dict()["id"] == project_id:
                is_project_found = True
                break
    # if user != db_project.created_by and user not in [project_user for project_user in [user_dict.user for user_dict in db_project.project_members]]:
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail="You don't have permission to update this project",
    #     )
    if not is_project_found:
        raise Exception("You don't have permission to access this project")
