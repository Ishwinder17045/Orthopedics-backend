from pydantic import BaseModel
from typing import Optional

class DoctorOut(BaseModel):
    id: int
    name: str
    specialty: str
    bio: Optional[str] = None
    photo_url: Optional[str] = None
    experience_years: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    available: bool

    class Config:
        from_attributes = True
