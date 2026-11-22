def student_report(students):
    for student in students:
        yield student

def faculty_report(faculty):
    for item in faculty:
        yield item

def course_report(courses):
    for course in courses:
        yield course

class StudentIterator:
    def __init__(self, students):
        self.students = students
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.students):
            raise StopIteration
        item = self.students[self.index]
        self.index += 1
        return item
