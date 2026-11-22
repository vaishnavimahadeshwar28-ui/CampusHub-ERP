from app.database import repository

def enroll_student(data):
    return repository.add_enrollment(data)

def remove_enrollment(record_id):
    return repository.delete_enrollment(record_id)

def list_enrollments():
    return repository.get_enrollments()
