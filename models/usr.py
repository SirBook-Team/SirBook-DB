from pydantic import BaseModel

class userData(BaseModel):
    email: str
    hashed_password: str
    firstname: str
    lastname: str
    gender: str
    dateOfBirth: str
    phoneNumber: str
