from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime
import os

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to grades
    grades = relationship("Grade", back_populates="student")
    
    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.first_name} {self.last_name}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'created_at': self.created_at.isoformat()
        }

class Course(Base):
    __tablename__ = 'courses'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    code = Column(String(10), unique=True, nullable=False)
    credits = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship to grades
    grades = relationship("Grade", back_populates="course")
    
    def __repr__(self):
        return f"<Course(id={self.id}, name='{self.name}', code='{self.code}')>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'credits': self.credits,
            'created_at': self.created_at.isoformat()
        }

class Grade(Base):
    __tablename__ = 'grades'
    
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_id = Column(Integer, ForeignKey('courses.id'), nullable=False)
    score = Column(Float, nullable=False)
    semester = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    student = relationship("Student", back_populates="grades")
    course = relationship("Course", back_populates="grades")
    
    def __repr__(self):
        return f"<Grade(id={self.id}, student_id={self.student_id}, course_id={self.course_id}, score={self.score})>"
    
    def to_dict(self):
        return {
            'id': self.id,
            'student_id': self.student_id,
            'course_id': self.course_id,
            'score': self.score,
            'semester': self.semester,
            'created_at': self.created_at.isoformat(),
            'student_name': f"{self.student.first_name} {self.student.last_name}",
            'course_name': self.course.name
        }
