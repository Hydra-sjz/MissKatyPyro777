
from sys import exit as exiter
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from misskaty.vars import DATABASE_URI as BDB_URI, LOGGER



if BDB_URI:
    try:
        BIRTHDAY_DB = MongoClient(BDB_URI)
    except PyMongoError as f:
        LOGGER.error(f"Error in Mongodb2: {f}")
        exiter(1)
    Birth_main_db = BIRTHDAY_DB["birthdays"]

    bday_info = Birth_main_db['users_bday']
    bday_cinfo = Birth_main_db["chat_bday"]

from datetime import datetime


def till_date(date):
    form = "%Y-%m-%d %H:%M:%S"
    z = datetime.strptime(date,form)
    return z
