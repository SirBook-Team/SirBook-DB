from pymongo import MongoClient
MongoClient = MongoClient('mongodb://localhost:27017/sirBook')
db = MongoClient.sirBook
collection = db.users
