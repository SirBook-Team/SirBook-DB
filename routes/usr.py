from fastapi import APIRouter, HTTPException ,Depends ,Request
from models.usr import userData, PostData, CommentData
from schemas.usr import  userEntity, postEntity, commentEntity, usersEntity, postsEntity, commentsEntity
from bson.objectid import ObjectId
from config.db import users_collection, posts_collection, comments_collection

router = APIRouter()

collections = {
    "users": users_collection,
    "posts": posts_collection,
    "comments": comments_collection
}

entities = {
    "users": userEntity,
    "posts": postEntity,
    "comments": commentEntity
}

entities_list = {
    "users": usersEntity,
    "posts": postsEntity,
    "comments": commentsEntity
}

models = {
    "users": userData,
    "posts": PostData,
    "comments": CommentData
}

def get_model(entity_type: str):
    if entity_type not in models:
        raise HTTPException(status_code=404, detail="Entity type not found")
    return models[entity_type]

@router.get('/{entity_type}')
async def find_all(entity_type: str):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    entities = collection.find()
    return entities_list[entity_type](entities)

@router.get('/{entity_type}/{entity_id}')
async def find_one(entity_type: str, entity_id: str):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    entity = collection.find_one({"_id": ObjectId(entity_id)})
    if entity:
        return entities[entity_type](entity)
    raise HTTPException(status_code=404, detail="Entity not found")

@router.post('/{entity_type}')
async def create(entity_type: str, request: Request):
    model = get_model(entity_type)
    entity = await request.json()
    entity = model(**entity)
    collection = collections[entity_type]
    entity_dict = entity.dict()
    collection.insert_one(entity_dict)
    return {"message": f"{entity_type[:-1].capitalize()} created successfully."}