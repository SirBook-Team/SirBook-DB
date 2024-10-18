from pymongo import MongoClient, ASCENDING
from bson.objectid import ObjectId
import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sirbook']

# Define Users collection schema
users_collection = db['users']
users_collection.create_index([("email", ASCENDING)], unique=True)

# Define Posts collection schema
posts_collection = db['posts']

# Define Comments collection schema
comments_collection = db['comments']

# Insert Sample Data
def insert_sample_data():
    user_id = str(ObjectId())
    post_id = str(ObjectId())
    comment_id = str(ObjectId())

    users_collection.insert_one({
        "usr_id": user_id,
        "email": "user@example.com",
        "password": "hashed_password",
        "friends_ids": [],
        "posts_ids": [post_id],
        "followers_ids": [],
        "following_ids": [],
        "profile_photo": "http://example.com/profile.jpg",
        "cover_photo": "http://example.com/cover.jpg",
        "description": "This is a user bio."
    })

    posts_collection.insert_one({
        "post_id": post_id,
        "author_id": user_id,
        "content": "This is a post content.",
        "comments_ids": [comment_id],
        "profiles_reacted_ids": [],
        "timestamp": datetime.datetime.now()
    })

    comments_collection.insert_one({
        "comment_id": comment_id,
        "post_id": post_id,
        "author_id": user_id,
        "content": "This is a comment content.",
        "timestamp": datetime.datetime.now()
    })

insert_sample_data()
print("Collections and sample documents created successfully.")