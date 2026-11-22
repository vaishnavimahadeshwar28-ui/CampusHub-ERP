from app.database import repository

def add_faculty(data):
    return repository.add_faculty(data)

def remove_faculty(record_id):
    return repository.delete_faculty(record_id)

def update_faculty(record_id, data):
    return repository.update_faculty(record_id, data)

def list_faculty():
    return repository.get_faculty()
