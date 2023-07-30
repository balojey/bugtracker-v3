from fastapi_users.authentication import AuthenticationBackend, JWTStrategy
from ..config import Settings
from .transport import bearer_transport
from .strategy import get_database_strategy


settings = Settings()


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(
        secret=settings.secret_key,
        lifetime_seconds=settings.access_token_expire_seconds,
    )


auth_backend = AuthenticationBackend(
    name="jwt", transport=bearer_transport, get_strategy=get_jwt_strategy
)
