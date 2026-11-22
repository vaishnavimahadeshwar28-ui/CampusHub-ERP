def test_enrollment_values():
    student_id = "ST001"
    course_code = "CS101"
    assert student_id.startswith("ST")
    assert course_code.startswith("CS")
