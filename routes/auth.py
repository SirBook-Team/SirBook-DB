from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from models import users_collection
from bson.objectid import ObjectId

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    hashed_password = generate_password_hash(password)
    user = {
        "usr_id": str(ObjectId()),
        "email": email,
        "password": hashed_password,
        "friends_ids": [],
        "posts_ids": [],
        "followers_ids": [],
        "following_ids": [],
        "profile_photo": "",
        "cover_photo": "",
        "description": ""
    }
    users_collection.insert_one(user)
    return jsonify({"message": "User registered successfully."}), 201

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    user = users_collection.find_one({"email": email})
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(identity=user['usr_id'])
        return jsonify({"token": access_token}), 200
    return jsonify({"message": "Invalid email or password."}), 401