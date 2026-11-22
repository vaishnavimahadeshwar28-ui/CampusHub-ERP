from app.core.descriptors import NonEmpty, Email, Age
from app.models.person import BasePerson
from app.core.metaclasses import ModelMeta

class Faculty(BasePerson, metaclass=ModelMeta):
    name = NonEmpty()
    email = Email()
    age = Age()

    def __init__(self, faculty_id, name, age, email, department):
        self.faculty_id = faculty_id
        self.name = name
        self.age = age
        self.email = email
        self.department = department
