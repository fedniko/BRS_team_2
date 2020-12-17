from Student import Student
from datetime import date


class Factory:
    def __str__(self):
        return Student(self.сode, self.fio, self.birthdate, self.email, self.phone)

    def create_student(code, fio, birthdate, email, phone):
        return code.__str__(), fio.__str__(), birthdate.__str__(), email.__str__(), phone.__str__()
