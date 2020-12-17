from Student import Student
from Group import Group
from Subject import Subject
from datetime import date


class Factory:
    def __init__(self):
        return Group(self.name, self.year)

    def __init__(self):
        return Subject(self.code, self.name)

    def __str__(self):
        return Student(self.сode, self.fio, self.birthdate, self.email, self.phone)

    def create_student(code, fio, birthdate, email, phone):
        return code.__str__(), fio.__str__(), birthdate.__str__(), email.__str__(), phone.__str__()

    def create_Gruop(name, year):
        return name.__init__(), year.__init__()

    def creat_Subject(code, name):
        return code.__init__(), name.__init__()