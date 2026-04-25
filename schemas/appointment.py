from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AppointmentCreate(BaseModel):
    patient_name: str
    email: EmailStr
    phone: str
    doctor_id: Optional[int] = None
    service_id: Optional[int] = None
    appointment_datetime: datetime
    notes: Optional[str] = None

class AppointmentOut(BaseModel):
    id: int
    patient_name: str
    email: EmailStr
    phone: str
    doctor_id: Optional[int] = None
    service_id: Optional[int] = None
    appointment_datetime: datetime
    notes: Optional[str] = None
    status: str

    class Config:
        from_attributes = True
