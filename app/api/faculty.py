from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import faculty_service
from app.core.validators import validate_email, validate_faculty_id

router = APIRouter(prefix="/faculty", tags=["Faculty"])

class FacultyInput(BaseModel):
    faculty_id: str
    name: str
    age: int
    email: str
    department: str

@router.get("/")
def get_faculty():
    return faculty_service.list_faculty()

@router.get("/{record_id}")
def get_one_faculty(record_id: int):
    result = next((x for x in faculty_service.list_faculty() if x.id == record_id), None)
    if not result:
        raise HTTPException(404, "Faculty not found")
    return result

@router.post("/")
def add_faculty(item: FacultyInput):
    if not validate_faculty_id(item.faculty_id):
        raise HTTPException(400, "Faculty ID must be like FC001")
    if not validate_email(item.email):
        raise HTTPException(400, "Invalid email")
    try:
        return faculty_service.add_faculty(item.model_dump())
    except Exception:
        raise HTTPException(400, "Faculty ID may already exist")

@router.put("/{record_id}")
def update_faculty(record_id: int, item: FacultyInput):
    result = faculty_service.update_faculty(record_id, item.model_dump())
    if not result:
        raise HTTPException(404, "Faculty not found")
    return result

@router.delete("/{record_id}")
def delete_faculty(record_id: int):
    if not faculty_service.remove_faculty(record_id):
        raise HTTPException(404, "Faculty not found")
    return {"message": "Faculty deleted"}
