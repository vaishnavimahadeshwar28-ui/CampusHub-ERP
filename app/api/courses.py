from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import course_service
from app.core.validators import validate_course_code

router = APIRouter(prefix="/courses", tags=["Courses"])

class CourseInput(BaseModel):
    course_code: str
    course_name: str
    credits: int

@router.get("/")
def get_courses():
    return course_service.list_courses()

@router.get("/{record_id}")
def get_one_course(record_id: int):
    result = next((x for x in course_service.list_courses() if x.id == record_id), None)
    if not result:
        raise HTTPException(404, "Course not found")
    return result

@router.post("/")
def add_course(item: CourseInput):
    if not validate_course_code(item.course_code):
        raise HTTPException(400, "Course Code must be like CS101")
    try:
        return course_service.add_course(item.model_dump())
    except Exception:
        raise HTTPException(400, "Course code may already exist")

@router.put("/{record_id}")
def update_course(record_id: int, item: CourseInput):
    result = course_service.update_course(record_id, item.model_dump())
    if not result:
        raise HTTPException(404, "Course not found")
    return result

@router.delete("/{record_id}")
def delete_course(record_id: int):
    if not course_service.remove_course(record_id):
        raise HTTPException(404, "Course not found")
    return {"message": "Course deleted"}
