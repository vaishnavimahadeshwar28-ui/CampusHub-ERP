
import os

from app.database import repository
from app.utils.file_manager import ReportWriter
from app.utils.generators import (
    student_report,
    faculty_report,
    course_report
)
from app.utils.logger import logger


def write_report(filename, title, records, generator):
    os.makedirs("reports", exist_ok=True)

    with ReportWriter(filename) as file:
        file.write(title + "\n")
        file.write("=" * 40 + "\n\n")

        for record in generator(records):
            for column in record.__table__.columns:
                value = getattr(record, column.name)
                file.write(f"{column.name}: {value}\n")

            file.write("\n")

    logger.info("%s generated successfully", filename)


def generate_all_reports():
    logger.info("Report generation started")

    try:
        students = repository.get_students()
        faculty = repository.get_faculty()
        courses = repository.get_courses()

        write_report(
            "reports/You.txt",
            "STUDENT REPORT",
            students,
            student_report
        )

        write_report(
            "reports/faculty.txt",
            "FACULTY REPORT",
            faculty,
            faculty_report
        )

        write_report(
            "reports/courses.txt",
            "COURSE REPORT",
            courses,
            course_report
        )

        logger.info("All reports generated successfully")
        print("All reports generated successfully!")

    except Exception:
        logger.exception("Report generation failed")
        raise


if __name__ == "__main__":
    generate_all_reports()
