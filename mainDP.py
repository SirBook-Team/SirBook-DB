from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sirBook']

# Define Users collection schema
users_collection = db['users']
users_collection.create_index([("email", ASCENDING)], unique=True)

# Define Posts collection schema
posts_collection = db['posts']

# Define Comments collection schema
comments_collection = db['comments']

#sample users
user1 = {
    "email": "try_email",
    "hashed_password": "try_password",
    "firstname": "try_firstname",
    "lastname": "try_lastname",
    "gender": "try_gender",
    "dateOfBirth": "try_dateOfBirth",
    "phoneNumber": "try_phoneNumber",
    "created_at": datetime.datetime.now(),
    "profile_picture_url": "try_profile_picture",
}



inserted_user = users_collection.insert_one(user1)
print("Collections and sample documents created successfully.")