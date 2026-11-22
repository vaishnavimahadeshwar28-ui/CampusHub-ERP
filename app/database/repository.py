from app.database.db import SessionLocal
from app.database.models import StudentDB, FacultyDB, CourseDB, EnrollmentDB

def add_student(data):
    return _add(StudentDB, data)

def get_students():
    return _all(StudentDB)

def get_student(record_id):
    return _get(StudentDB, record_id)

def update_student(record_id, data):
    return _update(StudentDB, record_id, data)

def delete_student(record_id):
    return _delete(StudentDB, record_id)

def add_faculty(data):
    return _add(FacultyDB, data)

def get_faculty():
    return _all(FacultyDB)

def update_faculty(record_id, data):
    return _update(FacultyDB, record_id, data)

def delete_faculty(record_id):
    return _delete(FacultyDB, record_id)

def add_course(data):
    return _add(CourseDB, data)

def get_courses():
    return _all(CourseDB)

def update_course(record_id, data):
    return _update(CourseDB, record_id, data)

def delete_course(record_id):
    return _delete(CourseDB, record_id)

def add_enrollment(data):
    return _add(EnrollmentDB, data)

def get_enrollments():
    return _all(EnrollmentDB)

def delete_enrollment(record_id):
    return _delete(EnrollmentDB, record_id)

def _add(model, data):
    db = SessionLocal()
    try:
        obj = model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    finally:
        db.close()

def _all(model):
    db = SessionLocal()
    try:
        return db.query(model).all()
    finally:
        db.close()

def _get(model, record_id):
    db = SessionLocal()
    try:
        return db.query(model).filter(model.id == record_id).first()
    finally:
        db.close()

def _update(model, record_id, data):
    db = SessionLocal()
    try:
        obj = db.query(model).filter(model.id == record_id).first()
        if not obj:
            return None
        for key, value in data.items():
            if value is not None and hasattr(obj, key):
                setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj
    finally:
        db.close()

def _delete(model, record_id):
    db = SessionLocal()
    try:
        obj = db.query(model).filter(model.id == record_id).first()
        if not obj:
            return False
        db.delete(obj)
        db.commit()
        return True
    finally:
        db.close()
