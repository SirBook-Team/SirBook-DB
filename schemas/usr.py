from models import *
from datetime import date

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
        "profile": item.get("profile", None)
    }

def postEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "owner": item["owner"],
        "content": item["content"],
        "comments_ids": item.get("comments_ids", []),
        "profiles_reacted_ids": item.get("profiles_reacted_ids", []),
        "timestamp": item.get("timestamp", date.today().strftime("%Y-%m-%d"))
    }

def commentEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "post_id": item["post_id"],
        "author_id": item["author_id"],
        "content": item["content"],
        "timestamp": item.get("timestamp", date.today().strftime("%Y-%m-%d"))
    }



def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]

def postsEntity(entity) -> list:
    return [postEntity(item) for item in entity]

def commentsEntity(entity) -> list:
    return [commentEntity(item) for item in entity]