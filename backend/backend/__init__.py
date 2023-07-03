import motor.motor_asyncio
from .config import Settings


settings = Settings()
client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.database_url, uuidRepresentation="standard"
)
db = client[settings.database_name]
