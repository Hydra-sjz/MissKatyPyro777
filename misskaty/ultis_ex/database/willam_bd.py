from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from misskaty.vars import DATABASE_URI

mongo_client = MongoClient(DATABASE_URI)
db = mongo_client.misskaty
