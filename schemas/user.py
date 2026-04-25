from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserSignupRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    username: str
    phone: str = None
    password: str

class UserLoginRequest(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    username: str
    phone: str = None
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True

class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user: UserOut
