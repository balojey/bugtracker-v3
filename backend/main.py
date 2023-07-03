from beanie import init_beanie
from fastapi import FastAPI
from backend import db
from backend.models import User, Bug, Project, Comment, File, ProjectMember
from backend.auth.models import AccessToken
from backend.users.routes import router as users_router
from backend.auth.routes import router as auth_router
from backend.projects.routes import router as projects_router


app = FastAPI()


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(projects_router)


@app.on_event("startup")
async def on_startup():
    """Startup event"""
    await init_beanie(
        database=db,
        document_models=[User, AccessToken, Bug, Project, Comment, File, ProjectMember],
    )
