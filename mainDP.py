from pymongo import MongoClient
import datetime

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['sirBook']

# Define Users collection schema
users_collection = db['users']
posts_collection = db['posts']
comments_collection = db['comments']

# Sample user document
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

# Insert user document
inserted_user = users_collection.insert_one(user1)
user_id = inserted_user.inserted_id

# Sample post document
post1 = {
    "author_id": str(user_id),
    "content": "This is a sample post content.",
    "comments_ids": [],
    "profiles_reacted_ids": [],
    "timestamp": datetime.datetime.now()
}

# Insert post document
inserted_post = posts_collection.insert_one(post1)
post_id = inserted_post.inserted_id

# Sample comment document
comment1 = {
    "post_id": str(post_id),
    "author_id": str(user_id),
    "content": "This is a sample comment content.",
    "timestamp": datetime.datetime.now()
}

# Insert comment document
inserted_comment = comments_collection.insert_one(comment1)
comment_id = inserted_comment.inserted_id

# Update post document with comment ID
posts_collection.update_one(
    {"_id": post_id},
    {"$push": {"comments_ids": str(comment_id)}}
)

print("Sample documents inserted successfully.")