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
async def find_all(entity_type: str, request: Request):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]

    parms = dict(request.query_params)
    if parms:
        entities = collection.find(parms)
    else:
        entities = collection.find()        

    print(parms)
    return entities_list[entity_type](entities)

@router.get('/{entity_type}/{entity_id}')
async def find_one(entity_type: str, entity_id: str):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    entity = collection.find_one({"_id": ObjectId(entity_id)})
    if entity is None:
        raise HTTPException(status_code=404, detail="Entity not found")
    print(entities[entity_type](entity))
    return entities[entity_type](entity)

@router.post('/{entity_type}')
async def create(entity_type: str, request: Request):
    model = get_model(entity_type)
    entity = await request.json()
    entity = model(**entity)
    collection = collections[entity_type]
    entity_dict = entity.dict()
    collection.insert_one(entity_dict)
    print(entity)
    # return created entity
    return entity

@router.put('/{entity_type}')
async def update(entity_type: str, request: Request):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    parms = dict(request.query_params)
    if not parms:
        raise HTTPException(status_code=400, detail="Query parameters are required for update")
    entity = await request.json()
    model = get_model(entity_type)
    entity = model(**entity)
    entity_dict = entity.dict()
    result = collection.update_many(parms, {"$set": entity_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": f"{entity_type[:-1].capitalize()} updated successfully."}

@router.put('/{entity_type}/{entity_id}')
async def update_one(entity_type: str, entity_id: str, request: Request):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    entity = await request.json()
    model = get_model(entity_type)
    entity = model(**entity)
    print(entity)
    entity_dict = entity.dict()
    result = collection.update_one({"_id": ObjectId(entity_id)}, {"$set": entity_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": f"{entity_type[:-1].capitalize()} updated successfully."}

@router.delete('/{entity_type}')
async def delete(entity_type: str, request: Request):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    parms = dict(request.query_params)
    if not parms:
        raise HTTPException(status_code=400, detail="Query parameters are required for delete")
    result = collection.delete_many(parms)
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": f"{entity_type[:-1].capitalize()} deleted successfully."}

@router.delete('/{entity_type}/{entity_id}')
async def delete_one(entity_type: str, entity_id: str):
    if entity_type not in collections:
        raise HTTPException(status_code=404, detail="Entity type not found")
    collection = collections[entity_type]
    result = collection.delete_one({"_id": ObjectId(entity_id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Entity not found")
    return {"message": f"{entity_type[:-1].capitalize()} deleted successfully."}
