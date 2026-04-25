from sqlalchemy.orm import Session
from database.connection import SessionLocal
from models.doctor import Doctor
from models.service import Service

DOCTOR_SEED = [
    {
        "name": "Dr. Richard James",
        "specialty": "Joint Replacement Specialist",
        "bio": "Board-certified orthopedic surgeon specializing in hip and knee replacement surgeries.",
        "photo_url": "https://images.unsplash.com/photo-1612349317150-e413f6a5b16d?q=80&w=800&auto=format&fit=crop",
        "experience_years": 20,
        "email": "richard.james@orthoplus.com",
        "phone": "+1-555-0101",
        "available": True,
    },
    {
        "name": "Dr. Sarah Johnson",
        "specialty": "Sports Medicine Expert",
        "bio": "Expert in ACL reconstruction, sports injury repair, and athletic rehabilitation.",
        "photo_url": "https://images.squarespace-cdn.com/content/v1/6015b67960bac64bcb525b15/2e55d8e5-6763-4a55-9d64-390b0b976ff4/sarah-johnson-edina-orthopedic-physical-therapist?format=2500w",
        "experience_years": 15,
        "email": "sarah.johnson@orthoplus.com",
        "phone": "+1-555-0102",
        "available": True,
    },
    {
        "name": "Dr. Michael Chen",
        "specialty": "Spine Surgeon",
        "bio": "Specializes in minimally invasive spine surgery and chronic back pain treatment.",
        "photo_url": "https://images.unsplash.com/photo-1622253692010-333f2da6031d?q=80&w=800&auto=format&fit=crop",
        "experience_years": 18,
        "email": "michael.chen@orthoplus.com",
        "phone": "+1-555-0103",
        "available": True,
    },
    {
        "name": "Dr. Emily Roberts",
        "specialty": "Pediatric Orthopedist",
        "bio": "Compassionate care for children with congenital and traumatic orthopedic conditions.",
        "photo_url": "https://images.unsplash.com/photo-1559839734-2b71ea197ec2?q=80&w=800&auto=format&fit=crop",
        "experience_years": 12,
        "email": "emily.roberts@orthoplus.com",
        "phone": "+1-555-0104",
        "available": True,
    },
    {
        "name": "Dr. David Kim",
        "specialty": "Fracture & Trauma Care",
        "bio": "Experienced trauma surgeon providing emergency fracture management and complex bone repair.",
        "photo_url": "https://images.unsplash.com/photo-1537368910025-700350fe46c7?q=80&w=800&auto=format&fit=crop",
        "experience_years": 16,
        "email": "david.kim@orthoplus.com",
        "phone": "+1-555-0105",
        "available": True,
    },
    {
        "name": "Dr. Lisa Patel",
        "specialty": "Physiotherapy & Rehabilitation",
        "bio": "Focuses on post-surgical rehabilitation and non-operative musculoskeletal recovery.",
        "photo_url": "https://images.unsplash.com/photo-1614608682850-e0d6ed316d47?q=80&w=800&auto=format&fit=crop",
        "experience_years": 10,
        "email": "lisa.patel@orthoplus.com",
        "phone": "+1-555-0106",
        "available": True,
    },
]

SERVICE_SEED = [
    {
        "title": "Joint Replacement",
        "summary": "Hip, knee, and shoulder replacement surgeries.",
        "description": "Comprehensive joint replacement options using advanced surgical techniques and robotic-assisted technology.",
        "category": "Orthopedic Surgery",
        "icon_url": "",
    },
    {
        "title": "Fracture & Trauma Care",
        "summary": "Emergency and scheduled fracture treatment.",
        "description": "Rapid assessment and fixation for bone fractures, trauma injuries, and complex orthopedic emergencies.",
        "category": "Trauma Care",
        "icon_url": "",
    },
    {
        "title": "Sports Injury Treatment",
        "summary": "Injury prevention and expert sports care.",
        "description": "Diagnosis, treatment, and rehabilitation for athletes suffering from sports-related injuries.",
        "category": "Sports Medicine",
        "icon_url": "",
    },
    {
        "title": "Spine Care & Back Pain",
        "summary": "Spinal health and pain management.",
        "description": "Conservative and surgical treatments for back pain, disc injuries, and spinal disorders.",
        "category": "Spine Care",
        "icon_url": "",
    },
    {
        "title": "Physiotherapy & Rehabilitation",
        "summary": "Recovery and strength rebuilding.",
        "description": "Personalized rehabilitation programs to restore mobility, strength, and function after injury or surgery.",
        "category": "Rehabilitation",
        "icon_url": "",
    },
    {
        "title": "Arthritis Treatment",
        "summary": "Joint preservation and pain relief.",
        "description": "Evidence-based arthritis care including medication management, injections, and surgical options.",
        "category": "Chronic Care",
        "icon_url": "",
    },
]


def seed_initial_data():
    session: Session = SessionLocal()
    try:
        doctor_count = session.query(Doctor).count()
        service_count = session.query(Service).count()

        if doctor_count == 0:
            session.add_all([Doctor(**doctor) for doctor in DOCTOR_SEED])
            print(f"Inserted {len(DOCTOR_SEED)} doctors")

        if service_count == 0:
            session.add_all([Service(**service) for service in SERVICE_SEED])
            print(f"Inserted {len(SERVICE_SEED)} services")

        if doctor_count == 0 or service_count == 0:
            session.commit()
    finally:
        session.close()


if __name__ == '__main__':
    seed_initial_data()
