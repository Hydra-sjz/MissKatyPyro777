# * @author        Yasir Aris M <yasiramunandar@gmail.com>
# * @date          2023-06-21 22:12:27
# * @projectName   MissKatyPyro
# * Copyright ©YasirPedia All rights reserved
import requests
import sys
from logging import getLogger
from os import environ
import pytz
import dotenv
import os

LOGGER = getLogger("MissKaty")

dotenv.load_dotenv("config.env", override=True)

if YT_COOKIES := environ.get("YT_COOKIES"):
    response = requests.get(YT_COOKIES)
    if response.status_code == 200:
        with open('cookies.txt', 'w') as file:
            file.write(response.text)
            LOGGER.info("Success download YT Cookies")
    else:
        LOGGER.info("Failed download YT Cookies")

if API_ID := environ.get("API_ID", ""):
    API_ID = int(API_ID)
else:
    LOGGER.error("API_ID variable is missing! Exiting now")
    sys.exit(1)
API_HASH = environ.get("API_HASH", "")
if not API_HASH:
    LOGGER.error("API_HASH variable is missing! Exiting now")
    sys.exit(1)
BOT_TOKEN = environ.get("BOT_TOKEN", "")
if not BOT_TOKEN:
    LOGGER.error("BOT_TOKEN variable is missing! Exiting now")
    sys.exit(1)
DATABASE_URI = environ.get("DATABASE_URI", "")
if not DATABASE_URI:
    LOGGER.error("DATABASE_URI variable is missing! Exiting now")
    sys.exit(1)
if LOG_CHANNEL := environ.get("LOG_CHANNEL", ""):
    LOG_CHANNEL = int(LOG_CHANNEL)

else:
    LOGGER.error("LOG_CHANNEL variable is missing! Exiting now")
    sys.exit(1)
# Optional ENV
LOG_GROUP_ID = environ.get("LOG_GROUP_ID")
USER_SESSION = environ.get("USER_SESSION")
DATABASE_NAME = environ.get("DATABASE_NAME", "MissKatyDB")
TZ = environ.get("TZ", "Asia/Kolkata")
PORT = environ.get("PORT", 80)
COMMAND_HANDLER = environ.get("COMMAND_HANDLER", "! /").split()
SUDO = list(
    {
        int(x)
        for x in environ.get(
            "SUDO",
            "784589736",
        ).split()
    }
)
OWNER_ID = int(environ.get("OWNER_ID", 784589736))
SUPPORT_CHAT = environ.get("SUPPORT_CHAT", "xbots_x")
AUTO_RESTART = environ.get("AUTO_RESTART", False)
GEMINI_API = environ.get("GEMINI_API")
GOOGLEAI_KEY = environ.get("GOOGLEAI_KEY")
PAYDISINI_KEY = environ.get("PAYDISINI_KEY")
PAYDISINI_CHANNEL_ID = environ.get("PAYDISINI_CHANNEL_ID", "17")

## Config For AUtoForwarder
# Forward From Chat ID
FORWARD_FROM_CHAT_ID = list(
    {
        int(x)
        for x in environ.get(
            "FORWARD_FROM_CHAT_ID",
            "-1001997285269",
        ).split()
    }
)
# Forward To Chat ID
FORWARD_TO_CHAT_ID = list(
    {int(x) for x in environ.get("FORWARD_TO_CHAT_ID", "-1002039074117").split()}
)
FORWARD_FILTERS = list(set(environ.get("FORWARD_FILTERS", "video document").split()))
BLOCK_FILES_WITHOUT_EXTENSIONS = bool(
    environ.get("BLOCK_FILES_WITHOUT_EXTENSIONS", True)
)
BLOCKED_EXTENSIONS = list(
    set(
        environ.get(
            "BLOCKED_EXTENSIONS",
            "html htm json txt php gif png ink torrent url nfo xml xhtml jpg",
        ).split()
    )
)
MINIMUM_FILE_SIZE = environ.get("MINIMUM_FILE_SIZE")
CURRENCY_API = environ.get("CURRENCY_API")

#time zone
TIME_ZONE = pytz.timezone('Asia/Kolkata')

#======ANILIST==========
ANILIST_CLIENT = os.environ.get("ANILIST_CLIENT")
ANILIST_SECRET = os.environ.get("ANILIST_SECRET")
ANILIST_REDIRECT_URL = os.environ.get("ANILIST_REDIRECT_URL", "https://anilist.co/api/v2/oauth/pin")
TRIGGERS = os.environ.get("TRIGGERS", "/ !").split()
BOT_NAME = os.environ.get("BOT_NAME", "@GojoSatoru_Xbot")

HELP_DICT = dict()


HELP_DICT[
    "Group"
] = """
Group based commands:
/anisettings - Toggle stuff like whether to allow 18+ stuff in group or whether to notify about aired animes, etc and change UI
/anidisable - Disable use of a cmd in the group (Disable multiple cmds by adding space between them)
`/anidisable anime anilist me user`
/anienable - Enable use of a cmd in the group (Enable multiple cmds by adding space between them)
`/anienable anime anilist me user`
/anidisabled - List out disabled cmds
"""

HELP_DICT[
    "Additional"
] = """Use /anireverse cmd to get reverse search via tracemoepy API
__Note: This works best on uncropped anime pic,
when used on cropped media, you may get result but it might not be too reliable__
Use /schedule cmd to get scheduled animes based on weekdays
Use /watch cmd to get watch order of searched anime
Use /anfillers cmd to get a list of fillers for an anime
Use /quote cmd to get a random quote
"""

HELP_DICT[
    "Anilist"
] = """
Below is the list of basic anilist cmds for info on anime, character, manga, etc.
/anime - Use this cmd to get info on specific anime using keywords (anime name) or Anilist ID
(Can lookup info on sequels and prequels)
/anilist - Use this cmd to choose between multiple animes with similar names related to searched query
(Doesn't includes buttons for prequel and sequel)
/character - Use this cmd to get info on character
/manga - Use this cmd to get info on manga
/airing - Use this cmd to get info on airing status of anime
/top - Use this cmd to lookup top animes of a genre/tag or from all animes
(To get a list of available tags or genres send /gettags or /getgenres
'/gettags nsfw' for nsfw tags)
/user - Use this cmd to get info on an anilist user
/browse - Use this cmd to get updates about latest animes
"""

HELP_DICT[
    "Oauth"
] = """
This includes advanced anilist features
Use /auth or !auth cmd to get details on how to authorize your Anilist account with bot
Authorising yourself unlocks advanced features of bot like:
- adding anime/character/manga to favourites
- viewing your anilist data related to anime/manga in your searches which includes score, status, and favourites
- unlock /flex, /ame, /activity and /favourites commands
- adding/updating anilist entry like completed or plan to watch/read
- deleting anilist entry
Use /flex or !flex cmd to get your anilist stats
Use /logout or !logout cmd to disconnect your Anilist account
Use /ame or !ame cmd to get your anilist recent activity
Can also use /activity or !activity
Use /favourites or !favourites cmd to get your anilist favourites
"""
