from app.core.validators import validate_course_code

def test_course_validation():
    assert validate_course_code("CS101")
