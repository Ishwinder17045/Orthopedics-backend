from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database.connection import get_db
from models.service import Service
from schemas.service import ServiceOut

router = APIRouter(prefix="/services", tags=["Services"])

@router.get("/", response_model=List[ServiceOut])
def get_services(db: Session = Depends(get_db)):
    return db.query(Service).order_by(Service.id).all()

@router.get("/{service_id}", response_model=ServiceOut)
def get_service(service_id: int, db: Session = Depends(get_db)):
    service = db.query(Service).filter(Service.id == service_id).first()
    if not service:
        raise HTTPException(status_code=404, detail="Service not found")
    return service
