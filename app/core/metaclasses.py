from datetime import datetime

class ModelMeta(type):
    def __new__(mcls, name, bases, namespace):
        namespace.setdefault("created_at", datetime.now())
        namespace.setdefault("updated_at", datetime.now())
        return super().__new__(mcls, name, bases, namespace)
