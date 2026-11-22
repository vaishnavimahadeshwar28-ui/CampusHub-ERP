from app.core.descriptors import NonEmpty
from app.core.metaclasses import ModelMeta

class Course(metaclass=ModelMeta):
    course_code = NonEmpty()
    course_name = NonEmpty()

    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits

    def to_dict(self):
        return self.__dict__.copy()
