from sqlalchemy import Column, Integer, String, Boolean, Text
from .base import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    specialty = Column(String(120), nullable=False)
    bio = Column(Text, nullable=True)
    photo_url = Column(String(255), nullable=True)
    experience_years = Column(Integer, nullable=True)
    email = Column(String(120), nullable=True)
    phone = Column(String(50), nullable=True)
    available = Column(Boolean, default=True)
