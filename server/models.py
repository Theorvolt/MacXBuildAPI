from pydantic import BaseModel, Field
from typing import Optional


class User(BaseModel):
    username: str 
    email: str 
    age: int = Field(...,gt=0)
    password: str

class UpdateUser(BaseModel):
    username: Optional[str] # str | None 
    email: Optional[str] 
    age: Optional[int] = Field(...,gt=0)
    password: Optional[str]