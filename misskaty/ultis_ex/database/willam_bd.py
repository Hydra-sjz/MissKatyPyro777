from async_pymongo import AsyncClient
from misskaty.vars import DATABASE_URI

mongo_client = AsyncClient(DATABASE_URI)
db = mongo_client.misskaty
