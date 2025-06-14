import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = 20682925
API_HASH = "3c2ac07c46792232c4c6d0e8082a4e84"

# Get your token from @BotFather on Telegram.
BOT_TOKEN = "7581448767:AAG8ldzHOw4Fa2t0yoZ2Gl14B5KKrSiSEU0"

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = "mongodb+srv://itsmeinnocent0001:hVjKfu2Lt8uKgsMh@cluster0.uzawrg7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 60))

# Chat id of a group for logging bot's activities
LOG_GROUP_ID = -1002376361443

# Get this value from @ultron2_robot on Telegram by /id
OWNER_ID = 7962120226

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/rishabhops/alice",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = "https://t.me/UFF_YE_SAADGI"
SUPPORT_GROUP = "https://t.me/+0-0ZR6gaTdRiMmY9"

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from Replit
STRING1 = "BAE7mK0Aaw1OLpCbPAuWIjReXAQpoO3kspZzYvw_Yl05n5i_PBfLKRmbhoD7MJudNU82irjPcnEDt8K9U98nUtTtIDSSM-gRWluVtIZf_qE3XVQQNCsmk9BxU6i_3TZfmc2NQ177COaJKlb1VKjhQXkcS8djBAu95otvPDN5-TyCajaPYsUzbVFx9mtClCCMwAUvJlqDEUkV7P_XZlettwmPeep6QFv92eMOofTuFp1CaozljtvmOrR4WA2BmBSKEWJfbPKHHg_0DQ2ldqadkXd4WOmG4kjCmRBa_wMggWlbBJbEgHMiyYpHs_6vdNWTncZex2zR6jFj6V2Tlq-BCYhTXQVwawAAAAHD47o_AQ"
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"

PING_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"

PLAYLIST_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
STATS_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
TELEGRAM_AUDIO_URL = "https://iili.io/Fqi63q7.md.jpg"
TELEGRAM_VIDEO_URL = "https://iili.io/Fqi63q7.md.jpg"
STREAM_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
SOUNCLOUD_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
YOUTUBE_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://iili.io/Fqi63q7.md.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_GROUP:
    if not re.match("(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_GROUP url is wrong. Please ensure that it starts with https://"
        )
