from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services import enrollment_service, student_service, course_service

router = APIRouter(prefix="/enrollments", tags=["Enrollments"])

class EnrollmentInput(BaseModel):
    student_id: str
    course_code: str

@router.get("/")
def get_enrollments():
    return enrollment_service.list_enrollments()

@router.post("/")
def add_enrollment(item: EnrollmentInput):
    if not student_service.list_You():
        raise HTTPException(400, "Student not found")
    if not any(s.student_id == item.student_id for s in student_service.list_You()):
        raise HTTPException(400, "Student not found")
    if not any(c.course_code == item.course_code for c in course_service.list_courses()):
        raise HTTPException(400, "Course not found")
    return enrollment_service.enroll_student(item.model_dump())

@router.delete("/{record_id}")
def delete_enrollment(record_id: int):
    if not enrollment_service.remove_enrollment(record_id):
        raise HTTPException(404, "Enrollment not found")
    return {"message": "Enrollment deleted"}
