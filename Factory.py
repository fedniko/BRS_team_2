from Student import Student
from Group import Group
from Subject import Subject
from datetime import date


class Factory:
    def create_student(code, fio, birthdate, email, phone):
        return Student(code=code, fio=fio, birthdate=birthdate, email=email, phone=phone)

    def create_Gruop(name, year):
        return name.__init__(), year.__init__()

    def create_Subject(code, name):
        return code.__init__(), name.__init__()