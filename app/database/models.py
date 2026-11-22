from sqlalchemy import Column, Integer, String
from app.database.db import Base

class StudentDB(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    department = Column(String, nullable=False)

class FacultyDB(Base):
    __tablename__ = "faculty"
    id = Column(Integer, primary_key=True)
    faculty_id = Column(String, unique=True, nullable=False)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    email = Column(String, nullable=False)
    department = Column(String, nullable=False)

class CourseDB(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True)
    course_code = Column(String, unique=True, nullable=False)
    course_name = Column(String, nullable=False)
    credits = Column(Integer, nullable=False)

class EnrollmentDB(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True)
    student_id = Column(String, nullable=False)
    course_code = Column(String, nullable=False)
