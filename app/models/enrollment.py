class Enrollment:
    def __init__(self, enrollment_id, student_id, course_code):
        self.enrollment_id = enrollment_id
        self.student_id = student_id
        self.course_code = course_code

    def to_dict(self):
        return self.__dict__.copy()
