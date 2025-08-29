from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from lib.models import Base
import os

# Database URL - using SQLite for simplicity
DATABASE_URL = "sqlite:///grademaster.db"

engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Initialize the database with tables"""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Get a database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

