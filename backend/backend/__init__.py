import motor.motor_asyncio
from .config import Settings
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


settings = Settings()
uri = settings.database_url
client = motor.motor_asyncio.AsyncIOMotorClient(
    settings.database_url, uuidRepresentation="standard"
)
db = client[settings.database_name]
