import re

def validate_email(email):
    return bool(re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email))

def validate_student_id(value):
    return bool(re.fullmatch(r"ST\d{3}", value))

def validate_faculty_id(value):
    return bool(re.fullmatch(r"FC\d{3}", value))

def validate_course_code(value):
    return bool(re.fullmatch(r"CS\d{3}", value))
