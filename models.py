from pymongo import MongoClient
from config import MONGO_URI

client = MongoClient(MONGO_URI)
db = client['sirbook']

users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']