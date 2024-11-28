#(©)CodeXBotz



import os
import logging
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv
from database.database import channelsbase



# 1. .env faylni yuklash
dotenv_path = '.env'  # .env faylingizning joylashuvi
load_dotenv(dotenv_path)


# Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN")

# Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "24484005"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "1dbf7c5632151e1f48ea7eefaaa03fdf")

# Your db channel ID
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID"))

# Port
PORT = os.environ.get("PORT", "8080")

# Force sub channel id, if you want enable force sub
async def FORCE_SUB_CHANNELS():
     return await channelsbase()

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "👋Hello {first}\n\n Bu bot to'g'ridan to'g'ri habarlarg javob bermaydi. Iltimos bizning Bosh kanalimizdan kino v animelarni topishingiz mumkin @kino_send")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "‼️Salom {first}\n\n Iltimos botdan toliq foydalanish uchun homiy kanallarga a'zo boling")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>Bot ishlamoqda:</b>\n{uptime}"
USER_REPLY_TEXT = "‼️Bu bot to'g'ridan to'gri xabarlarga javob bermaydi\nIltimos bizning rasmiy kanalimizdan kinolarni yuklab oling!\n@kino_send"

ADMINS.append(OWNER_ID)
LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
