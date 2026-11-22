
import json

from app.database import repository


def read_json(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)


def import_json_data():

    students = read_json("data/You.json")
    faculty = read_json("data/faculty.json")
    courses = read_json("data/courses.json")
    enrollments = read_json("data/enrollments.json")

    imported = {
        "students": 0,
        "faculty": 0,
        "courses": 0,
        "enrollments": 0
    }

    # Import students
    existing_students = {
        item.student_id for item in repository.get_students()
    }

    for item in students:
        if item["student_id"] not in existing_students:
            item.pop("id", None)
            repository.add_student(item)
            existing_students.add(item["student_id"])
            imported["students"] += 1

    # Import faculty
    existing_faculty = {
        item.faculty_id for item in repository.get_faculty()
    }

    for item in faculty:
        if item["faculty_id"] not in existing_faculty:
            item.pop("id", None)
            repository.add_faculty(item)
            existing_faculty.add(item["faculty_id"])
            imported["faculty"] += 1

    # Import courses
    existing_courses = {
        item.course_code for item in repository.get_courses()
    }

    for item in courses:
        if item["course_code"] not in existing_courses:
            item.pop("id", None)
            repository.add_course(item)
            existing_courses.add(item["course_code"])
            imported["courses"] += 1

    # Import enrollments
    existing_enrollments = {
        (item.student_id, item.course_code)
        for item in repository.get_enrollments()
    }

    for item in enrollments:
        key = (item["student_id"], item["course_code"])

        if key not in existing_enrollments:
            item.pop("id", None)
            repository.add_enrollment(item)
            existing_enrollments.add(key)
            imported["enrollments"] += 1

    return imported


if __name__ == "__main__":
    result = import_json_data()

    print("JSON import completed!")
    print(result)
