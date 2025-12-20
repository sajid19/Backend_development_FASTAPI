from typing import Union
from fastapi import FastAPI, HTTPException , Query
from uuid import UUID
from .schemas.user import  User , UserCreate , UserListResponse , ShowModel, AuthUser
from .core.database import create_db_and_tables , SessionDep
from model.model import CreateUser 
from sqlmodel import  select
from typing import Annotated

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

@app.get("/user")
def read_root(session: SessionDep, offset:int=0,  limit: Annotated[int, Query(le=100)] = 100, sort:int|None = None , )-> UserListResponse:
    userList = session.exec(select(User).offset(offset).limit(limit)).all()
    return UserListResponse(
        users=userList,
        count=len(userList)
    )

@app.get("/user/{id}",  response_model=ShowModel)
def read_user_details(id: UUID, session: SessionDep ) -> User:
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


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




@app.post("/auth/user")
def auth_user(user: AuthUser , session: SessionDep):
    db_user = CreateUser(**user.dict())
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return {"authuser": db_user, "message": "User created successfully"}