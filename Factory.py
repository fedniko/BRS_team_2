from Student import Student
from Group import Group
from Subject import Subject
from datetime import date
import time


def create_student(code, fio, birthdate, email, phone):
    if code == '':
        raise Exception('Код не может быть пустым')
    elif not code.isdigit():
        raise Exception('Код студента должен содержать только цифры')
    else:
        new_code = int(code)
    if fio == '':
        raise Exception('ФИО не может быть пустым')
    elif fio == ' ':
        raise Exception('ФИО не может быть пробелом')
    elif ' ' not in fio:
        raise Exception('Введите Фамилию и Имя')
    if birthdate == '':
        raise Exception('Дата рождения не может быть пустым')
    else:
        try:
            time.strptime(birthdate, '%d.%m.%Y')
        except ValueError:
            raise ValueError('Введите дату в формате ДД.ММ.ГГГГ')

    return Student(code=new_code, fio=fio, birthdate=birthdate, email=email, phone=phone)


def create_subject(code, name):
    if code == '':
        raise Exception('Код не может быть пустым')
    elif not code.isupper():
        raise Exception('Код предмета должен содержать только заглавные буквы')
    elif code == ' ':
        raise Exception('Код предмета не может быть пробелом')
    if name == '':
        raise Exception('Название предмета не может быть пустым')
    elif name == ' ':
        raise Exception('Название предмета не может быть пробелом')


    return Subject(code, name)

class Factory:
    def create_Group(name, year):
        return name.__init__(), year.__init__()

