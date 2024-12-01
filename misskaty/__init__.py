# * @author        Yasir Aris M <yasiramunandar@gmail.com>
# * @date          2023-06-21 22:12:27
# * @projectName   MissKatyPyro
# * Copyright ©YasirPedia All rights reserved
import os
import time
from asyncio import get_event_loop
from faulthandler import enable as faulthandler_enable
from logging import ERROR, INFO, StreamHandler, basicConfig, getLogger, handlers
import logging
import uvloop, uvicorn
from apscheduler.jobstores.mongodb import MongoDBJobStore
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from async_pymongo import AsyncClient
from pymongo import MongoClient
from pyrogram import Client
from web.webserver import api
from telegraph import Telegraph
from telethon import TelegramClient
#from telegram.ext import Application
from aiohttp import ClientSession
#from motor.motor_asyncio import AsyncIOMotorClient
from misskaty.vars import (
    API_HASH,
    API_ID,
    BOT_TOKEN,
    DATABASE_NAME,
    DATABASE_URI,
    PORT,
    TZ,
    USER_SESSION,
)

telegraph = Telegraph(domain="graph.org")
#telegraph.create_account(short_name=BOT_USERNAME)

from Python_ARQ import ARQ

# Aiohttp Async Client
session = ClientSession()
ARQ_API_KEY = "UGYUYZ-XUPAZN-AHPELZ-SBQMPQ-ARQ"  # GET API KEY FROM @ARQRobot
ARQ_API_URL = "arq.hamker.dev"

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, session)

# enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

LOGGER = logging.getLogger(__name__)

basicConfig(
    level=INFO,
    format="[%(levelname)s] - [%(asctime)s - %(name)s - %(message)s] -> [%(module)s:%(lineno)d]",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        handlers.RotatingFileHandler(
            "MissKatyLogs.txt", mode="w+", maxBytes=5242880, backupCount=1
        ),
        StreamHandler(),
    ],
)
getLogger("pyrogram").setLevel(ERROR)
getLogger("openai").setLevel(ERROR)
getLogger("httpx").setLevel(ERROR)
getLogger("iytdl").setLevel(ERROR)

MOD_LOAD = []
MOD_NOLOAD = ["subscene_dl"]
HELPABLE = {}
cleanmode = {}
botStartTime = time.time()
misskaty_version = "v2.16.1"
DEV_USERS = [2021523124, 784589736] 
DOWN_PATH = "app/downloads/"
DOWN_PATH2 = "anilist/downloads/"
uvloop.install()
faulthandler_enable()
from misskaty.core import misskaty_patch

from motor import motor_asyncio
#from motor.motor_asyncio import AsyncIOMotorClient

mongo = motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
db = mongo["Gojo"]

#Telethon bot
tle = TelegramClient("telethn", API_ID, API_HASH, flood_sleep_threshold=0).start(bot_token=BOT_TOKEN)
print("⚫⚪TELETHON IS STARTED...⚫⚪")

from motor.motor_asyncio import AsyncIOMotorClient
from telegram.ext import Application

application = Application.builder().token(BOT_TOKEN).build()
print("🔵🔵Python Telegram Bot Txt IS STARTED...🔵🔵")

lol = AsyncIOMotorClient(DATABASE_URI)
dbw = lol['Character_catcher']
collection = dbw['anime_characters_lol']
user_totals_collection = dbw['user_totals_lmaoooo']
user_collection = dbw["user_collection_lmaoooo"]
group_user_totals_collection = dbw['group_user_totalsssssss']
top_global_groups_collection = dbw['top_global_groups']
pm_users = dbw['total_pm_users']
safari_cooldown_collection = dbw["safari_cooldown"]
safari_users_collection = dbw["safari_users_collection"]
sudo_users_collection= dbw["sudo_users_collection"]
registered_users = dbw['registered_users']
set_on_data = dbw['set_on_data']
refeer_collection = dbw['refeer_collection']
set_off_data = dbw['set_off_data']

# Pyrogram Bot Client
app = Client(
    "GojoSaturoBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=True),
    sleep_threshold=180,
    app_version="MissKatyPyro Stable",
    workers=50,
    max_concurrent_transmissions=4,
)
app.db = AsyncClient(DATABASE_URI)
app.log = getLogger("🟢🟢Gojo Saturo is Started...🟢🟢")

# Pyrogram UserBot Client
user = Client(
    "YasirUBot",
    session_string=USER_SESSION,
    mongodb=dict(connection=AsyncClient(DATABASE_URI), remove_peers=False),
    sleep_threshold=180,
    app_version="GoJo Ubot",
)

jobstores = {
    "default": MongoDBJobStore(
        client=MongoClient(DATABASE_URI), database=DATABASE_NAME, collection="nightmode"
    )
}
scheduler = AsyncIOScheduler(jobstores=jobstores, timezone=TZ)

async def run_wsgi():
    config = uvicorn.Config(api, host="0.0.0.0", port=int(PORT))
    server = uvicorn.Server(config)
    await server.serve()

app.start()
BOT_ID = app.me.id
BOT_NAME = app.me.first_name
BOT_USERNAME = app.me.username
if USER_SESSION:
    try:
        user.start()
        UBOT_ID = user.me.id
        UBOT_NAME = user.me.first_name
        UBOT_USERNAME = user.me.username
    except Exception as e:
        app.log.error(f"Error while starting UBot: {e}")
        UBOT_ID = None
        UBOT_NAME = None
        UBOT_USERNAME = None
else:
    UBOT_ID = None
    UBOT_NAME = None
    UBOT_USERNAME = None
