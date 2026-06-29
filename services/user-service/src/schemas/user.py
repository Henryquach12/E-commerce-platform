from pydantic import BaseModel, EmailStr
from uuid import UUID
from datetime import datetime

class UserCreate(BaseModel):
    user_name: str
    full_name: str
    phone_number: str
    address: str
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: UUID
    user_name: str
    full_name: str
    phone_number: str
    address: str
    email: EmailStr
    created_at: datetime
    is_active: bool
    