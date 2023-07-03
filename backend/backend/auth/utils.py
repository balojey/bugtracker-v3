from fastapi_users_db_beanie.access_token import BeanieAccessTokenDatabase
from .models import AccessToken


async def get_access_token_db():
    yield BeanieAccessTokenDatabase(AccessToken)
