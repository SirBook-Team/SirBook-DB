from pymongo import MongoClient
MongoClient = MongoClient('mongodb://localhost:27017/sirBook')
db = MongoClient.sirBook
users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']
