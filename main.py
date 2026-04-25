from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database.connection import engine
from models.base import Base
from models import base
from models.doctor import Doctor
from models.service import Service
from models.appointment import Appointment
from models.contact_message import ContactMessage
from models.testimonial import Testimonial
from models.user import User
from routes import doctors, services, appointments, contact, testimonials, news, auth
from seed import seed_initial_data

app = FastAPI(title="Orthopaedics Healthcare API")

origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    "http://localhost:5175",
    "http://127.0.0.1:5175",
    "https://orthofrontend.vercel.app"   # ← your production frontend
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(doctors.router)
app.include_router(services.router)
app.include_router(appointments.router)
app.include_router(contact.router)
app.include_router(testimonials.router)
app.include_router(news.router)
app.include_router(auth.router)

base.Base.metadata.create_all(bind=engine)
seed_initial_data()

@app.get("/")
def home():
    return {"message": "Orthopaedic API is running "}
