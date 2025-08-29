from sqlalchemy.orm import sessionmaker
from lib.database import engine, init_db
from lib.models import Student, Course, Grade
from lib.helpers import validate_email, calculate_average, get_pass_fail_status

class GradeMasterCLI:
    def __init__(self):
        init_db()
        self.session = sessionmaker(bind=engine)()

    def run(self):
        menu = {"1":self.add_student, "2":self.add_course, "3":self.add_grade, "4":self.view_student_performance, "5":self.update_student, "6":self.delete_student, "7":self.view_top_students, "8":self.list_students, "9":self.list_courses}
        
        while True:
            print("\n1.Add Student 2.Add Course 3.Add Grade 4.View Performance 5.Update Student 6.Delete Student 7.Top Students 8.List Students 9.List Courses 0.Exit")
            choice = input("Choice: ")
            if choice == '0': break
            if choice in menu: menu[choice]()
            else: print("Invalid choice")

    def add_student(self):
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        if not validate_email(email) or self.session.query(Student).filter_by(email=email).first():
            print("Invalid email or already exists")
            return
        self.session.add(Student(first_name=first_name, last_name=last_name, email=email))
        self.session.commit()
        print("Student added")

    def add_course(self):
        name = input("Course Name: ")
        code = input("Course Code: ").upper()
        credits = int(input("Credits: "))
        if self.session.query(Course).filter_by(code=code).first():
            print("Course already exists")
            return
        self.session.add(Course(name=name, code=code, credits=credits))
        self.session.commit()
        print("Course added")

    def add_grade(self):
        students = self.session.query(Student).all()
        courses = self.session.query(Course).all()
        if not students or not courses:
            print("Need students and courses first")
            return
        for s in students: print(f"{s.id}. {s.first_name} {s.last_name}")
        student_id = int(input("Student ID: "))
        for c in courses: print(f"{c.id}. {c.name}")
        course_id = int(input("Course ID: "))
        score = float(input("Score: "))
        semester = input("Semester: ")
        if 0 <= score <= 100:
            self.session.add(Grade(student_id=student_id, course_id=course_id, score=score, semester=semester))
            self.session.commit()
            print("Grade added")
        else: print("Invalid score")

    def view_student_performance(self):
        students = self.session.query(Student).all()
        if not students: return print("No students")
        for s in students: print(f"{s.id}. {s.first_name} {s.last_name}")
        student_id = int(input("Student ID: "))
        student = self.session.query(Student).get(student_id)
        if not student: return print("Student not found")
        grades = self.session.query(Grade).filter_by(student_id=student_id).all()
        if not grades: return print("No grades")
        for g in grades: print(f"{g.course.name}: {g.score}%")
        avg = calculate_average([g.score for g in grades])
        print(f"Average: {avg:.1f}% - {get_pass_fail_status(avg)}")

    def update_student(self):
        students = self.session.query(Student).all()
        if not students: return print("No students")
        for s in students: print(f"{s.id}. {s.first_name} {s.last_name}")
        student = self.session.query(Student).get(int(input("Student ID: ")))
        if not student: return print("Not found")
        first_name = input(f"First Name ({student.first_name}): ")
        last_name = input(f"Last Name ({student.last_name}): ")
        email = input(f"Email ({student.email}): ")
        if first_name: student.first_name = first_name
        if last_name: student.last_name = last_name
        if email and validate_email(email): student.email = email
        self.session.commit()
        print("Updated")

    def delete_student(self):
        students = self.session.query(Student).all()
        if not students: return print("No students")
        for s in students: print(f"{s.id}. {s.first_name} {s.last_name}")
        student = self.session.query(Student).get(int(input("Student ID: ")))
        if not student: return print("Not found")
        if input(f"Delete {student.first_name}? (y/N): ").lower() == 'y':
            self.session.delete(student)
            self.session.commit()
            print("Deleted")

    def view_top_students(self):
        students = self.session.query(Student).all()
        student_averages = []
        for student in students:
            grades = self.session.query(Grade).filter_by(student_id=student.id).all()
            if grades:
                avg = calculate_average([g.score for g in grades])
                student_averages.append((student, avg))
        if not student_averages: return print("No grades")
        student_averages.sort(key=lambda x: x[1], reverse=True)
        for i, (s, avg) in enumerate(student_averages[:5], 1):
            print(f"{i}. {s.first_name} {s.last_name}: {avg:.1f}% - {get_pass_fail_status(avg)}")

    def list_students(self):
        students = self.session.query(Student).all()
        if not students: return print("No students")
        for s in students: print(f"{s.id}. {s.first_name} {s.last_name} - {s.email}")

    def list_courses(self):
        courses = self.session.query(Course).all()
        if not courses: return print("No courses")
        for c in courses: print(f"{c.id}. {c.code} - {c.name} ({c.credits} credits)")

    def __del__(self):
        if hasattr(self, 'session'): self.session.close()