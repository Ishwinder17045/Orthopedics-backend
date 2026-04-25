from pydantic import BaseModel
from datetime import datetime

class TestimonialOut(BaseModel):
    id: int
    patient_name: str
    rating: int
    message: str
    created_at: datetime

    class Config:
        from_attributes = True
