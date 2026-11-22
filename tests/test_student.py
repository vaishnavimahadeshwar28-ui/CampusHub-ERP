
from app.core.validators import validate_student_id, validate_email


def test_valid_student_id():
    assert validate_student_id("ST001")


def test_invalid_student_id():
    assert not validate_student_id("ABC001")


def test_valid_email():
    assert validate_email("student@example.com")


def test_invalid_email():
    assert not validate_email("studentexample.com")


def test_student_id_format():
    assert not validate_student_id("ST01")
    assert not validate_student_id("ST0001")
