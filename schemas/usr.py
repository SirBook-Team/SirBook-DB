def userEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "email": item["email"],
        "hashed_password": item["hashed_password"],
        "firstname": item["firstname"],
        "lastname": item["lastname"],
        "gender": item["gender"],
        "dateOfBirth": item["dateOfBirth"],
        "phoneNumber": item["phoneNumber"]
    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]