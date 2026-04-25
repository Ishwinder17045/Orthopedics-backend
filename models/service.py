from sqlalchemy import Column, Integer, String, Text
from .base import Base

class Service(Base):
    __tablename__ = "services"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(140), nullable=False)
    summary = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    category = Column(String(100), nullable=True)
    icon_url = Column(String(255), nullable=True)
