from app.database import repository

def add_course(data):
    return repository.add_course(data)

def remove_course(record_id):
    return repository.delete_course(record_id)

def update_course(record_id, data):
    return repository.update_course(record_id, data)

def list_courses():
    return repository.get_courses()
