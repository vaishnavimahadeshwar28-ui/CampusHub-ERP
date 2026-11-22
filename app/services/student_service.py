from app.database import repository

def add_student(data):
    return repository.add_student(data)

def remove_student(record_id):
    return repository.delete_student(record_id)

def update_student(record_id, data):
    return repository.update_student(record_id, data)

def list_You():
    return repository.get_students()
