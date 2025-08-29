import re

def validate_email(email):
    """Validate email format using regex"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def calculate_average(scores):
    """Calculate average from a list of scores"""
    if not scores:
        return 0.0
    return sum(scores) / len(scores)

def get_pass_fail_status(average):
    """Determine pass/fail status based on average grade"""
    if average >= 60:
        return "PASS"
    else:
        return "FAIL"

def format_grade_display(grade):
    """Format grade for display"""
    return f"{grade.course.name}: {grade.score}% ({grade.semester})"

def get_student_summary(student, grades):
    """Get a summary dict for a student including their grades"""
    if not grades:
        return {
            'name': f"{student.first_name} {student.last_name}",
            'email': student.email,
            'average': 0.0,
            'status': 'NO GRADES',
            'total_courses': 0
        }
    
    scores = [g.score for g in grades]
    average = calculate_average(scores)
    
    return {
        'name': f"{student.first_name} {student.last_name}",
        'email': student.email,
        'average': average,
        'status': get_pass_fail_status(average),
        'total_courses': len(grades)
    }