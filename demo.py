#!/usr/bin/env python3
"""
Demo script to populate the database with sample data
"""

from sqlalchemy.orm import sessionmaker
from lib.database import engine, init_db
from lib.models import Student, Course, Grade

def create_sample_data():
    """Create sample students, courses, and grades"""
    
    # Initialize database
    init_db()
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Clear existing data
    session.query(Grade).delete()
    session.query(Student).delete()
    session.query(Course).delete()
    session.commit()
    
    # Create sample students
    students = [
        Student(first_name="Alice", last_name="Johnson", email="alice@example.com"),
        Student(first_name="Bob", last_name="Smith", email="bob@example.com"),
        Student(first_name="Carol", last_name="Davis", email="carol@example.com"),
        Student(first_name="David", last_name="Wilson", email="david@example.com"),
    ]
    
    # Create sample courses
    courses = [
        Course(name="Mathematics", code="MATH101", credits=3),
        Course(name="Physics", code="PHYS101", credits=4),
        Course(name="Chemistry", code="CHEM101", credits=3),
        Course(name="Biology", code="BIOL101", credits=4),
    ]
    
    # Add students and courses
    for student in students:
        session.add(student)
    for course in courses:
        session.add(course)
    session.commit()
    
    # Create sample grades
    grades_data = [
        # Alice's grades (excellent student)
        (1, 1, 95.0, "Fall 2024"),  # Alice, Math, 95%
        (1, 2, 92.0, "Fall 2024"),  # Alice, Physics, 92%
        (1, 3, 88.0, "Fall 2024"),  # Alice, Chemistry, 88%
        
        # Bob's grades (good student)
        (2, 1, 78.0, "Fall 2024"),  # Bob, Math, 78%
        (2, 2, 82.0, "Fall 2024"),  # Bob, Physics, 82%
        (2, 4, 85.0, "Fall 2024"),  # Bob, Biology, 85%
        
        # Carol's grades (average student)
        (3, 1, 65.0, "Fall 2024"),  # Carol, Math, 65%
        (3, 3, 70.0, "Fall 2024"),  # Carol, Chemistry, 70%
        (3, 4, 68.0, "Fall 2024"),  # Carol, Biology, 68%
        
        # David's grades (struggling student)
        (4, 1, 45.0, "Fall 2024"),  # David, Math, 45%
        (4, 2, 52.0, "Fall 2024"),  # David, Physics, 52%
    ]
    
    for student_id, course_id, score, semester in grades_data:
        grade = Grade(student_id=student_id, course_id=course_id, score=score, semester=semester)
        session.add(grade)
    
    session.commit()
    session.close()
    
    print("✅ Sample data created successfully!")
    print("\nSample Students:")
    print("1. Alice Johnson (alice@example.com) - Excellent student")
    print("2. Bob Smith (bob@example.com) - Good student") 
    print("3. Carol Davis (carol@example.com) - Average student")
    print("4. David Wilson (david@example.com) - Struggling student")
    
    print("\nSample Courses:")
    print("1. Mathematics (MATH101) - 3 credits")
    print("2. Physics (PHYS101) - 4 credits")
    print("3. Chemistry (CHEM101) - 3 credits")
    print("4. Biology (BIOL101) - 4 credits")
    
    print("\n🎓 Now run 'python main.py' to explore the application!")

if __name__ == "__main__":
    create_sample_data()