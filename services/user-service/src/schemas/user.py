from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime
from typing import Optional

# Schema for creating a new user; password is accepted in plain text and should be hashed before persistence.
class UserCreate(BaseModel):
    user_name: str
    full_name: str
    phone_number: str
    address: str
    email: EmailStr
    password: str

# Schema for returning user data in API responses; excludes sensitive fields like password.
class UserResponse(BaseModel):
    id: UUID
    user_name: str
    full_name: str
    phone_number: str
    address: str
    email: EmailStr
    created_at: datetime
    is_active: bool

# Schema for partial user updates; all fields optional so only provided fields are changed.
class UserUpdate(BaseModel):
    user_name: Optional[str] = None
    full_name: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    email: Optional[str] = None
    