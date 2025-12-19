from sqlmodel import Field, SQLModel 

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    description: str | None = Field(default=None, index=True) 


class CreateUser(SQLModel):
    __tablename__ = "api_user"
    name: str = Field(index=True)
    email: str | None = Field(default=None, index=True)
    password: str | None = Field(default=None, index=True)
    