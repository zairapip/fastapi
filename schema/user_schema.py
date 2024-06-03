from pydantic import BaseModel
from typing import Optional

class UserSchemaP (BaseModel):
    name: str
    surname: str
    email: str
    password_hash: str
    username: str
    telephone: str

class UserSchemaG (BaseModel):
    id: int
    name: str
    surname: str
    email: str
    password_hash: str
    username: str
    telephone: str

class UserSchemaE(BaseModel):
    error: str
