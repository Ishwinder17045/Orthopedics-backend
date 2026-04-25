from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database.connection import get_db
from models.testimonial import Testimonial
from schemas.testimonial import TestimonialOut

router = APIRouter(prefix="/testimonials", tags=["Testimonials"])

@router.get("/", response_model=List[TestimonialOut])
def get_testimonials(db: Session = Depends(get_db)):
    return db.query(Testimonial).order_by(Testimonial.created_at.desc()).all()
