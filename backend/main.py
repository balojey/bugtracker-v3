from beanie import init_beanie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend import db
from backend.models import User, Bug, Project, Comment, File, ProjectMember
from backend.auth.models import AccessToken
from backend.users.routes import router as users_router
from backend.auth.routes import router as auth_router
from backend.projects.routes import router as projects_router
from backend.project_members.routes import router as project_members_router
from backend.bugs.routes import router as bugs_router
from backend.comments.routes import router as comments_router
from backend.files.routes import router as files_router


app = FastAPI()


origins = [
        "http://localhost:3000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(projects_router)
app.include_router(project_members_router)
app.include_router(bugs_router)
app.include_router(comments_router)
app.include_router(files_router)


@app.on_event("startup")
async def on_startup():
    """Startup event"""
    await init_beanie(
        database=db,
        document_models=[User, AccessToken, Bug, Project, Comment, File, ProjectMember],
    )
