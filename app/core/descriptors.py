class NonEmpty:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, owner=None):
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not value or not str(value).strip():
            raise ValueError("Value cannot be empty")
        setattr(obj, self.name, value)


class Email:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, owner=None):
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if "@" not in value:
            raise ValueError("Invalid email")
        setattr(obj, self.name, value)


class Age:
    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, obj, owner=None):
        return getattr(obj, self.name, None)

    def __set__(self, obj, value):
        if not 16 <= value <= 80:
            raise ValueError("Age must be between 16 and 80")
        setattr(obj, self.name, value)
