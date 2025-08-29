# GradeMaster CLI - Student Grade Tracking Application

A simple command-line interface application for tracking student grades and performance.

## Features

- ✅ Add students and their details to database
- ✅ Add subjects/courses and assign grades to students  
- ✅ View student performance across all subjects
- ✅ Update or delete student information and grades
- ✅ Calculate student average grade and pass/fail status
- ✅ View top-performing students based on grades
- ✅ Persist all data in SQLite database

## Requirements

- Python 3.12+
- SQLAlchemy
- Alembic

## Installation

1. Install dependencies:
```bash
pipenv install
```

2. Activate virtual environment:
```bash
pipenv shell
```

## Usage

Run the application:
```bash
python main.py
```

## Database Schema

The application uses 3 related tables:

1. **Students** - stores student information
2. **Courses** - stores course/subject information  
3. **Grades** - stores grades linking students to courses

## Menu Options

1. Add Student
2. Add Course
3. Add Grade
4. View Student Performance
5. Update Student
6. Delete Student
7. View Top Students
8. List All Students
9. List All Courses
0. Exit

## Data Structures Used

- **Lists**: Used for storing collections of students, courses, and grades
- **Dictionaries**: Used in model `to_dict()` methods for data serialization
- **Tuples**: Used for sorting student averages in top performers feature

## Project Structure

```
grademaster-cli/
├── lib/
│   ├── __init__.py
│   ├── models.py      # SQLAlchemy models
│   ├── database.py    # Database configuration
│   ├── cli.py         # CLI interface
│   └── helpers.py     # Helper functions
├── main.py            # Application entry point
├── Pipfile            # Dependencies
└── README.md          # This file
```