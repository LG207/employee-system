from pydantic import BaseModel, constr

class UserCreate(BaseModel):
    username: str
    password: constr(min_length=6, max_length=72)

class UserLogin(BaseModel):
    username: str
    password: str