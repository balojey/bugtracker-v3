from httpx_oauth.clients.google import GoogleOAuth2
from ..config import Settings


settings = Settings()
google_oauth_client = GoogleOAuth2(
    settings.google_client_id, settings.google_client_secret
)
