from fastapi import APIRouter

from models.usr import userData
from config.db import collection , MongoClient
from schemas.usr import userEntity , usersEntity

user = APIRouter()

@user.get('/')
async def find_all_users():
    user = collection.find()
    return usersEntity(user)

@user.post('/')
async def create_user(user: userData):
    user = user.dict()
    inserted_user = collection.insert_one(user)
    return userEntity(user)