import os
import asyncio
from os import getenv
from dotenv import load_dotenv
from distutils.util import strtobool as sb
from requests import get
from telethon.sessions import StringSession
from telethon.sync import TelegramClient, custom, events
from pathlib import Path

load_dotenv()

BOT_TOKEN = os.environ.get("BOT_TOKEN")
STRING = getenv("STRING")
STRING2 = getenv("STRING2")
STRING3 = getenv("STRING3")
STRING4 = getenv("STRING4")
STRING5 = getenv("STRING5")
STRING6 = getenv("STRING6")
STRING7 = getenv("STRING7")
STRING8 = getenv("STRING8")
STRING9 = getenv("STRING9")
STRING10 = getenv("STRING10")
STRING11 = getenv("STRING11")
STRING12 = getenv("STRING12")
STRING13 = getenv("STRING13")
STRING14 = getenv("STRING14")
STRING15 = getenv("STRING15")
STRING16 = getenv("STRING16")
STRING17 = getenv("STRING17")
STRING18 = getenv("STRING18")
STRING19 = getenv("STRING19")
STRING20 = getenv("STRING20")
STRING21 = getenv("STRING21")
STRING22 = getenv("STRING22")
STRING23 = getenv("STRING23")
STRING24 = getenv("STRING24")
STRING25 = getenv("STRING25")
STRING26 = getenv("STRING26")
STRING27 = getenv("STRING27")
STRING28 = getenv("STRING28")
STRING29 = getenv("STRING29")
STRING30 = getenv("STRING30")
STRING31 = getenv("STRING31")
STRING32 = getenv("STRING32")
STRING33 = getenv("STRING33")
STRING34 = getenv("STRING34")
STRING35 = getenv("STRING35")
STRING36 = getenv("STRING36")
STRING37 = getenv("STRING37")
STRING38 = getenv("STRING38")
STRING39 = getenv("STRING39")
STRING40 = getenv("STRING40")
STRING41 = getenv("STRING41")
STRING42 = getenv("STRING42")
STRING43 = getenv("STRING43")
STRING44 = getenv("STRING44")
STRING45 = getenv("STRING45")
STRING46 = getenv("STRING46")
STRING47 = getenv("STRING47")
STRING48 = getenv("STRING48")
STRING49 = getenv("STRING49")
STRING50 = getenv("STRING50")
STRING51 = getenv("STRING51")
STRING52 = getenv("STRING52")
STRING53 = getenv("STRING53")
STRING54 = getenv("STRING54")
STRING55 = getenv("STRING55")
STRING56 = getenv("STRING56")
STRING57 = getenv("STRING57")
STRING58 = getenv("STRING58")
STRING59 = getenv("STRING59")
STRING60 = getenv("STRING60")
STRING61 = getenv("STRING61")
STRING62 = getenv("STRING62")
STRING63 = getenv("STRING63")
STRING64 = getenv("STRING64")
STRING65 = getenv("STRING65")
STRING66 = getenv("STRING66")
STRING67 = getenv("STRING67")
STRING68 = getenv("STRING68")
STRING69 = getenv("STRING69")
STRING70 = getenv("STRING70")
STRING71 = getenv("STRING71")
STRING72 = getenv("STRING72")
STRING73 = getenv("STRING73")
STRING74 = getenv("STRING74")
STRING75 = getenv("STRING75")
STRING76 = getenv("STRING76")
STRING77 = getenv("STRING77")
STRING78 = getenv("STRING78")
STRING79 = getenv("STRING79")
STRING80 = getenv("STRING80")
STRING81 = getenv("STRING81")
STRING82 = getenv("STRING82")
STRING83 = getenv("STRING83")
STRING84 = getenv("STRING84")
STRING85 = getenv("STRING85")
STRING86 = getenv("STRING86")
STRING87 = getenv("STRING87")
STRING88 = getenv("STRING88")
STRING89 = getenv("STRING89")
STRING90 = getenv("STRING90")
STRING91 = getenv("STRING91")
STRING92 = getenv("STRING92")
STRING93 = getenv("STRING93")
STRING94 = getenv("STRING94")
STRING95 = getenv("STRING95")
STRING96 = getenv("STRING96")
STRING97 = getenv("STRING97")
STRING98 = getenv("STRING98")
STRING99 = getenv("STRING99")
STRING100 = getenv("STRING100")

API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")
BIO_MESSAGE = getenv("BIO")
SUDO = set(int(x) for x in os.environ.get("SUDO", "").split())
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY") or None
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
UPSTREAM_REPO = getenv("UPSTREAM_REPO")

HNDLR = os.environ.get("HNDLR", r"\!")
BOT_HNDLR = os.environ.get("BOT_HNDLR", r"\!")
REPO_LINK = getenv("REPO_LINK")
ALIVE_NAME = os.environ.get("ALIVE_NAME") or "@AlphaXproject"
HASH_CHAT = getenv("HASH_CHAT")
ALIVE_LOGO = os.environ.get("ALIVE_LOGO") or None
TEMP_DOWNLOAD_DIRECTORY = os.environ.get(
    "TMP_DOWNLOAD_DIRECTORY") or "./downloads"
# Custom (forked) repo URL for updater.
UPSTREAM_REPO_URL = (os.environ.get("UPSTREAM_REPO_URL")
                    or "https://github.com/UserXTester/HyperAlphaX.git")

# UPSTREAM_REPO_URL branch, the default is master
UPSTREAM_REPO_BRANCH = os.environ.get("UPSTREAM_REPO_BRANCH", "HyperAlphaX")
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY") or None

# Logging channel/group ID configuration.
BOTLOG_CHATID = int(os.environ.get("BOTLOG_CHATID") or None)

# Userbot logging feature switch.
BOTLOG = sb(os.environ.get("BOTLOG") or "False")
LOGSPAMMER = sb(os.environ.get("LOGSPAMMER") or "True")


if STRING:
    # pylint: disable=invalid-name
    bot = TelegramClient(StringSession(STRING), API_ID, API_HASH)
else:
    # pylint: disable=invalid-name
    bot = TelegramClient("userbot", API_ID, API_HASH)


async def check_botlog_chatid():
    if not BOTLOG_CHATID and LOGSPAMMER:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the private error log storage to work."
        )
        sys.exit(1)

    elif not BOTLOG_CHATID and BOTLOG:
        LOGS.info(
            "You must set up the BOTLOG_CHATID variable in the config.env or environment variables, for the userbot logging feature to work."
        )
        sys.exit(1)

    elif not BOTLOG or not LOGSPAMMER:
        return

    entity = await bot.get_entity(BOTLOG_CHATID)
    if entity.default_banned_rights.send_messages:
        LOGS.info(
            "Your account doesn't have rights to send messages to BOTLOG_CHATID "
            "group. Check if you typed the Chat ID correctly.")
        sys.exit(1)
