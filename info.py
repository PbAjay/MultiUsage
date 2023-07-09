import re
import os
from os import environ

id_pattern = re.compile(r'^.\d+$')

BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", ""))
API_HASH = os.environ.get("API_HASH", "")
PICS = os.environ.get("PICS", "").split()
ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
DB_URL = os.environ.get("DB_URL", "")
DB_NAME = os.environ.get("DB_NAME", "tg-multi-bot")
RemoveBG_API = os.environ.get("RemoveBG_API", "")
FORCE_SUB = os.environ.get("FORCE_SUB", None)           
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", "")
log_channel = environ.get("LOG_CHANNEL")
LOG_CHANNEL = int(log_channel) if log_channel and id_pattern.search(log_channel) else None
LOG_TEXT = """<i><u>ᴜsᴇʀ ᴅᴇᴛᴀɪʟs</u>

○ ᴜsᴇʀ ɪᴅ : <code>{id}</code>
○ ᴅᴄ : <code>{dc_id}</code>
○ ɴᴀᴍᴇ : <code>{first_name}<code>
○ ᴜsᴇʀɴᴀᴍᴇ : @{username}

ʙʏ = {bot}</i>"""











