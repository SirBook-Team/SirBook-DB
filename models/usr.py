from pydantic import BaseModel

class userData(BaseModel):
    email: str
    hashed_password: str
    firstname: str
    lastname: str
    gender: str
    dateOfBirth: str
    phoneNumber: str

class PostData(BaseModel):
    author_id: str
    content: str
    comments_ids: list
    profiles_reacted_ids: list
    timestamp: str

class CommentData(BaseModel):
    post_id: str
    author_id: str
    content: str
    timestamp: str