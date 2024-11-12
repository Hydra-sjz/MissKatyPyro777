 # below code is taken from USERGE-X repo
# all credits to the respective author (dunno who wrote it will find later
# n update

#from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
#from motor.motor_asyncio import AsyncIOMotorClient

#from async_pymongo import AsyncClient
#from misskaty.vars import DATABASE_URI as MONGO_DB_URL

#MGCLIENT = AsyncClient(MONGO_DB_URL)
#DATABASE = MGCLIENT["Emilia"]


#def get_collection(name: str):
#    """Create or Get Collection from your database"""
#    return DATABASE[name]

__all__ = ["get_collection"]

from motor.core import AgnosticClient, AgnosticCollection, AgnosticDatabase
from motor.motor_asyncio import AsyncIOMotorClient

from misskaty.vars import DATABASE_URI as MONGO_DB_URL

_MGCLIENT: AgnosticClient = AsyncIOMotorClient(MONGO_DB_URL)

_DATABASE: AgnosticDatabase = _MGCLIENT["Gojo"]


def get_collection(name: str) -> AgnosticCollection:
    """Create or Get Collection from your database"""
    return _DATABASE[name]
