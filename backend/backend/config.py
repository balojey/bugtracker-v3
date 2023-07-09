from pydantic import BaseSettings
from dotenv import load_dotenv
from os import getenv


load_dotenv(".env")


class Settings(BaseSettings):
    """App settings"""

    app_name: str = "BugTracker"
    secret_key: str = "e6b7ab0df9425e60f30586abbf81d13aa6ee4aa2005096dc0e54658d4c61293f"    #getenv("SECRET_KEY")
    algorithm: str = "HS256"    #getenv("ALGORITHM")
    access_token_expire_seconds: int = 3600 * 24 * 7    #getenv("ACCESS_TOKEN_EXPIRE_SECONDS")
    database_url: str = "mongodb://localhost:27017" #getenv("DATABASE_URL")
    database_name: str = "bug_tracker"  #getenv("DATABASE_NAME")
    google_client_id: str = "418248972238-to9uii1lslvc71hm7sjv2d3878rttr5q.apps.googleusercontent.com"  #getenv("GOOGLE_CLIENT_ID")
    google_client_secret: str = "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"   #getenv("GOOGLE_CLIENT_SECRET")
    github_client_id: str = "3432372f72f25c5080eb"
    github_client_secret: str = "c5257592e77a79cde18f152f517e64cbaac47ef8"

    class Config:
        env_file = ".env"
