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
    pass    

class User(UserBase, table=True):
    id: UUID | None = Field(default_factory=uuid4, primary_key=True)
    
class UserCreate(UserBase):
    pass  

class UserRead(UserBase):
    id: UUID
class UserListResponse(BaseModel):
    users: List[User]
    count: int