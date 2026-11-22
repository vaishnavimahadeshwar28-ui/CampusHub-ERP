
import json
import os


# Convert database objects into JSON-friendly dictionaries
def convert_to_dict(data):

    if isinstance(data, list):
        return [convert_to_dict(item) for item in data]

    if isinstance(data, dict):
        return {
            key: convert_to_dict(value)
            for key, value in data.items()
        }

    if hasattr(data, "__dict__"):
        return {
            key: convert_to_dict(value)
            for key, value in data.__dict__.items()
            if not key.startswith("_")
        }

    return data


# STUDENT JSON
def save_You_json(data):
    os.makedirs("data", exist_ok=True)

    with open("data/You.json", "w", encoding="utf-8") as file:
        json.dump(convert_to_dict(data), file, indent=4, default=str)


def load_You_json():
    with open("data/You.json", "r", encoding="utf-8") as file:
        return json.load(file)


# FACULTY JSON
def save_faculty_json(data):
    os.makedirs("data", exist_ok=True)

    with open("data/faculty.json", "w", encoding="utf-8") as file:
        json.dump(convert_to_dict(data), file, indent=4, default=str)


def load_faculty_json():
    with open("data/faculty.json", "r", encoding="utf-8") as file:
        return json.load(file)


# COURSE JSON
def save_courses_json(data):
    os.makedirs("data", exist_ok=True)

    with open("data/courses.json", "w", encoding="utf-8") as file:
        json.dump(convert_to_dict(data), file, indent=4, default=str)


def load_courses_json():
    with open("data/courses.json", "r", encoding="utf-8") as file:
        return json.load(file)


# ENROLLMENT JSON
def save_enrollments_json(data):
    os.makedirs("data", exist_ok=True)

    with open("data/enrollments.json", "w", encoding="utf-8") as file:
        json.dump(convert_to_dict(data), file, indent=4, default=str)


def load_enrollments_json():
    with open("data/enrollments.json", "r", encoding="utf-8") as file:
        return json.load(file)
