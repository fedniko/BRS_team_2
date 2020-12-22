from Student import Student
from Group import Group
from Subject import Subject
from datetime import date


def create_student(code, fio, birthdate, email, phone):
    if code == '':
        raise Exception('Код не может быть пустым')
    elif not code.isdigit():
        raise Exception('Код студента должен содержать только цифры')
    else:
        new_code = int(code)
    return Student(code=new_code, fio=fio, birthdate=birthdate, email=email, phone=phone)


class Factory:
    def create_Group(name, year):
        return name.__init__(), year.__init__()

    def create_Subject(code, name):
        return Subject(code=code, name=name)
