from pathlib import Path
from sqlalchemy import create_engine
from sqlmodel import  Session , SQLModel
from typing import Annotated
from fastapi import Depends

BASE_DIR = Path(__file__).parent.parent.parent
DATABASE_URL = f"sqlite:///{BASE_DIR / 'database' / 'user.db'}"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)



def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]