import pytest
from backend import client
from beanie import init_beanie
from backend.models import User, Bug, Project, Comment, File, ProjectMember


@pytest.fixture
async def setup_db():
    db = client["test_db"]
    await init_beanie(
        database=db,
        document_models=[User, Bug, Project, Comment, File, ProjectMember],
    )
