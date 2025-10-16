from typing import Union
from fastapi import FastAPI, HTTPException
from uuid import UUID
from .schemas.user import  User , UserCreate
from .core.database import create_db_and_tables , SessionDep

app = FastAPI()
@app.on_event("startup")

def on_startup():
    create_db_and_tables()
    




DisplayUSER = []

@app.post("/create/user")
def create_user(user: UserCreate , session: SessionDep):
    user_create = User.from_orm(user)
    session.add(user_create)
    session.commit()
    session.refresh(user_create)
    return {"user": user_create, "message": "User created successfully"}

@app.get("/user/list")
def read_root(limit:int=10, sort:int|None = None):
    print(limit ,"limitt")
    print(sort)
    return DisplayUSER 



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
