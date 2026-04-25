from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.sql import func
from .base import Base

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String(120), nullable=False)
    email = Column(String(120), nullable=False)
    phone = Column(String(50), nullable=False)
    doctor_id = Column(Integer, ForeignKey("doctors.id"), nullable=True)
    service_id = Column(Integer, ForeignKey("services.id"), nullable=True)
    appointment_datetime = Column(DateTime(timezone=True), nullable=False)
    notes = Column(Text, nullable=True)
    status = Column(String(50), nullable=False, default="pending")
    created_at = Column(DateTime(timezone=True), server_default=func.now())
