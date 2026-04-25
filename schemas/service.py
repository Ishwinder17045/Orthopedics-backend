from pydantic import BaseModel
from typing import Optional

class ServiceOut(BaseModel):
    id: int
    title: str
    summary: Optional[str] = None
    description: Optional[str] = None
    category: Optional[str] = None
    icon_url: Optional[str] = None

    class Config:
        from_attributes = True
