from typing import Union
from fastapi import FastAPI, HTTPException
from uuid import UUID
from .schemas.user import UserCreate

app = FastAPI()



DisplayUSER = []

@app.get("/user/list")
def read_root(limit:int=10, sort:int|None = None):
    print(limit ,"limitt")
    print(sort)
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
