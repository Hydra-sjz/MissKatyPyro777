from async_pymongo import AsyncClient
from misskaty.vars import DATABASE_URI, DATABASE_NAME

mongo_client = AsyncClient(DATABASE_URI)
db = mongo_client.misskaty


from motor.motor_asyncio import AsyncIOMotorClient as MongoClient


mongo = MongoClient(DATABASE_URI)
dbname = mongo[DATABASE_NAME]
