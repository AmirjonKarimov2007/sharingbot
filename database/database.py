#(©)CodeXBotz




import pymongo, os
from dotenv import load_dotenv

dotenv_path = '.env'  # .env faylingizning joylashuvi
load_dotenv(dotenv_path)

# Database 
DB_URI = os.environ.get("DATABASE_URL")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")


dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]


user_data = database['users']
fschannels = database['channels']


async def add_channel(channel_id):
    fschannels.insert_one({'_id': channel_id})
    return

async def channelsbase():
    all_channels = fschannels.find()
    channel_ids = []
    for id in all_channels:
        channel_ids.append(id['_id'])
    return channel_ids

async def present_channel(channel_id):
    found = fschannels.find_one({'_id': channel_id})
    return bool(found)

async def del_channel(channel_id):
    fschannels.delete_one({'_id': channel_id})
    return


async def present_user(user_id : int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def full_userbase():
    user_docs = user_data.find()
    user_ids = []
    for doc in user_docs:
        user_ids.append(doc['_id'])
        
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return
