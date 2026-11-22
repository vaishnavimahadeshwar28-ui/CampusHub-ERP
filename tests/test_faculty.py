from app.core.validators import validate_faculty_id

def test_faculty_validation():
    assert validate_faculty_id("FC001")
