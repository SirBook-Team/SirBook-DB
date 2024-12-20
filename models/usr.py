from pydantic import BaseModel

class userData(BaseModel):
    email: str
    hashedPassword: str
    firstname: str
    lastname: str
    gender: str
    dateOfBirth: str
    phoneNumber: str
    profile: str

class PostData(BaseModel):
    owner: str
    content: str
    comments_ids: list
    profiles_reacted_ids: list
    timestamp: str
    image: str

class CommentData(BaseModel):
    post_id: str
    owner: str
    content: str
    timestamp: str