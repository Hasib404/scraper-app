from pymongo import mongo_client
from config import settings

client = mongo_client.MongoClient(settings.DATABASE_URL)

db_client = client[settings.MONGO_INITDB_DATABASE]
URL = db_client.urls
