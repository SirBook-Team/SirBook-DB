from models import *

def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "hashedPassword": item["hashedPassword"],
        "firstname": item["firstname"],
        "lastname": item["lastname"],
        "gender": item["gender"],
        "dateOfBirth": item["dateOfBirth"],
        "phoneNumber": item["phoneNumber"],
        "profile": item["profile"]
    }

def postEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "author_id": item["author_id"],
        "content": item["content"],
        "comments_ids": item["comments_ids"],
        "profiles_reacted_ids": item["profiles_reacted_ids"],
        "timestamp": item["timestamp"]
    }

def commentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "post_id": item["post_id"],
        "author_id": item["author_id"],
        "content": item["content"],
        "timestamp": item["timestamp"]
    }



def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]

def commentsEntity(entity) -> list:
    return [commentEntity(item) for item in entity]