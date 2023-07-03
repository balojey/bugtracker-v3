from fastapi_users_db_beanie.access_token import BeanieBaseAccessToken
from fastapi_users.db import BaseOAuthAccount
from beanie import Document


class AccessToken(BeanieBaseAccessToken, Document):
    pass


class OAuthAccount(BaseOAuthAccount):
    pass