from app import app
from extensions import db
from models import Course


courses = [
    Course(
        name="Python Programming for Beginners",
        subject="Programming",
        grade=8,
        price=1500,
        teacher="Rahul Sharma",
        rating=4.8
    ),
    Course(
        name="Advanced Python Development",
        subject="Programming",
        grade=10,
        price=2500,
        teacher="Priya Mehta",
        rating=4.9
    ),
    Course(
        name="Mathematics Fundamentals",
        subject="Mathematics",
        grade=6,
        price=1000,
        teacher="Amit Patil",
        rating=4.5
    ),
    Course(
        name="Algebra Masterclass",
        subject="Mathematics",
        grade=8,
        price=1800,
        teacher="Sneha Joshi",
        rating=4.7
    ),
    Course(
        name="Physics Made Easy",
        subject="Physics",
        grade=9,
        price=2000,
        teacher="Vikram Singh",
        rating=4.6
    ),
    Course(
        name="Introduction to Chemistry",
        subject="Chemistry",
        grade=8,
        price=1600,
        teacher="Neha Kapoor",
        rating=4.4
    ),
    Course(
        name="English Grammar & Writing",
        subject="English",
        grade=7,
        price=900,
        teacher="Anjali Deshmukh",
        rating=4.3
    ),
    Course(
        name="Creative Writing for Students",
        subject="English",
        grade=9,
        price=1300,
        teacher="Riya Shah",
        rating=4.8
    ),
    Course(
        name="Web Development Basics",
        subject="Programming",
        grade=10,
        price=2200,
        teacher="Arjun Rao",
        rating=4.9
    ),
    Course(
        name="Science Experiments at Home",
        subject="Science",
        grade=6,
        price=800,
        teacher="Karan Gupta",
        rating=4.2
    ),
    Course(
        name="Biology for Grade 10",
        subject="Biology",
        grade=10,
        price=1900,
        teacher="Meera Nair",
        rating=4.7
    ),
    Course(
        name="Geometry Essentials",
        subject="Mathematics",
        grade=7,
        price=1200,
        teacher="Rohan Kulkarni",
        rating=4.6
    )
]


with app.app_context():
    db.session.add_all(courses)
    db.session.commit()

    print("Courses added successfully!")