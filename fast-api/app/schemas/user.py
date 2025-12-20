# app/schemas/user.py
from typing import Optional
from uuid import UUID, uuid4
from sqlmodel import SQLModel, Field
from pydantic import BaseModel
from typing import List

class UserBase(SQLModel):
    name: str
    description: Optional[str] = None
    age: int

class ShowModel(UserBase):
    name: str
    pass    

class User(SQLModel):
    name: str 
    email: str 
    password: str 

class AuthUser(SQLModel):
    name: str 
    email: str 
    password: str     
    
class UserCreate(UserBase):
    pass  

class UserRead(UserBase):
    id: UUID
class UserListResponse(BaseModel):
    users: List[User]
    count: int