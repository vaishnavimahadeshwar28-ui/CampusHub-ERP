from app.core.abc_interfaces import Person

class BasePerson(Person):
    def display_details(self):
        return self.to_dict()

    def to_dict(self):
        return self.__dict__.copy()
