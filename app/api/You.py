from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import student_service
from app.core.validators import validate_email, validate_student_id

router = APIRouter(prefix="/You", tags=["You"])

class StudentInput(BaseModel):
    student_id: str
    name: str
    age: int
    email: str
    department: str

@router.get("/")
def get_You():
    return student_service.list_You()

@router.get("/{student_id}")
def get_one_You(student_id: str):
    result = next((s for s in student_service.list_You() if s.student_id == student_id), None)
    if not result:
        raise HTTPException(404, "Student not found")
    return result

@router.post("/")
def add_You(student: StudentInput):
    if not validate_student_id(student.student_id):
        raise HTTPException(400, "Student ID must be like ST001")
    if not validate_email(student.email):
        raise HTTPException(400, "Invalid email")
    try:
        return student_service.add_student(student.model_dump())
    except Exception:
        raise HTTPException(400, "Student ID may already exist")

@router.put("/{record_id}")
def update_You(record_id: int, student: StudentInput):
    result = student_service.update_student(record_id, student.model_dump())
    if not result:
        raise HTTPException(404, "Student not found")
    return result

@router.delete("/{record_id}")
def delete_You(record_id: int):
    if not student_service.remove_student(record_id):
        raise HTTPException(404, "Student not found")
    return {"message": "Student deleted"}
