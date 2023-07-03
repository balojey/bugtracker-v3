from fastapi_users.db import BeanieUserDatabase
from ..models import User


async def get_user_db():
    yield BeanieUserDatabase(User)


async def find_user_by_id(user_id: str) -> User:
    """A function to find a user by id"""
    user = await User.get(user_id)
    if user:
        return user
    raise Exception("User not found")


async def find_user_by_email(email: str) -> User:
    """A function to find a user by email"""
    user = await User.find_one(User.email == email)
    if user:
        return user
    raise Exception("User not found")


async def find_user_by_project(project_id: str):
    """A function to find a user by project"""
    users = User.find()
    async for user in users:
        if not user.created_projects:
            continue
        projects = [dico.to_dict() for dico in user.created_projects]
        print(projects)
        if not projects:
            continue
        for project in projects:
            print("project: ", project)
            if project["id"] == project_id:
                return user, projects.index(project)
    
    # if user:
    #     return user
    # raise Exception("User not found")
