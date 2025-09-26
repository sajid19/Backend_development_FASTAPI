from pydantic import BaseModel, Field
from uuid import UUID


class UserCreate(BaseModel):
    id: UUID
    name: str = Field(..., min_length=3, max_length=50)
    description: str = Field(..., max_length=300)
    age: int = Field(..., ge=0, le=120)