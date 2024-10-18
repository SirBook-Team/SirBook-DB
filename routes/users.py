from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import users_collection

users = Blueprint('users', __name__)

@users.route('/<usr_id>', methods=['GET'])
@jwt_required()
def get_user(usr_id):
    user = users_collection.find_one({"usr_id": usr_id})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    return jsonify({"message": "User not found."}), 404