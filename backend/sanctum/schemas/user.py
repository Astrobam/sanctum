# backend/sanctum/schemas/user.py

from pydantic import BaseModel, EmailStr
from datetime import datetime
import uuid

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return via API
class User(UserBase):
    user_id: uuid.UUID
    created_at: datetime

    class Config:
        from_attributes = True
