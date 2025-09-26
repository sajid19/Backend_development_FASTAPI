from typing import Union
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

class UserCreate(BaseModel):
    id: UUID
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=300)
    age: int = Field(..., ge=0, le=120)

DisplayUSER = []

@app.get("/user/list")
def read_root():
    return DisplayUSER


@app.post("/create/user")
def create_user(user: UserCreate):
    DisplayUSER.append(user)
    return {"user": user, "message": "User created successfully"}

@app.put("/update/user/{user_id}")
def update_user(user_id: UUID, user: UserCreate):
    for index, existing_user in enumerate(DisplayUSER):
        if existing_user.id == user_id:
            DisplayUSER[index] = user
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/delete/user/{user_id}")
def delete_user(user_id: UUID):
    for index, existing_user in enumerate(DisplayUSER):
        if existing_user.id == user_id:
            del DisplayUSER[index]
            return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
