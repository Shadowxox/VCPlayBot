import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN", "7476853493:AAEX4XE4SSLt72tgsXToPDMtRXYGZqWxhaY")
BOT_NAME = getenv("BOT_NAME", "𝐵𝑒𝑡𝑎 ꭙꤪꤨ 𝓜𝓾𝓼𝓲𝓬 🎶 🎵")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "hwkwjieie")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/9b13ea3ce046a1a5c8098.png")
admins = {}
API_ID = int(getenv("API_ID", "23287799"))
API_HASH = getenv("API_HASH", "9f4f17dae2181ee22c275b9b40a3c907")
BOT_USERNAME = getenv("BOT_USERNAME", "Beta_X_Music_Bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ll_Your_Shadow_ll")
OWNER_NAME = getenv("OWNER_NAME", "ll_Your_Shadow_ll")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "hwkwjieie")
PROJECT_NAME = getenv("PROJECT_NAME", "VCPlayBot2.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/QueenArzoo/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", "DBZ_LOG_GC")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7795212861").split()))
