from Student import Student
from Group import Group
from Subject import Subject
from EducationYear import EducationYear
from Crosssection import CrossSection
from BRSPoints import BRSPoints
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


def create_group(name, year):
    if name == '':
        raise Exception('Группа не может быть пустым')
    elif not name.isupper():
        raise Exception('Группа должен содержать только заглавные буквы')
    elif name == ' ':
        raise Exception('Группа предмета не может быть пробелом')
    if year == '':
        raise Exception('Год не может быть пустым')
    elif year == ' ':
        raise Exception('Год не может быть пробелом')
    elif not year.isdigit():
        raise Exception('Год не должен содержать буквы')

    return Group(name, year)


def create_BRSPoints(student: Student, subject: Subject, year: EducationYear, cross_section: CrossSection, points: int):
    if student is None:
        raise Exception('Объект класса Student не передан')
    elif type(student) != Student:
        raise Exception('Тип переданных данных не совпадает с классом Student ')
    if subject is None:
        raise Exception('Объект класса Subject не передан')
    elif type(subject) != Subject:
        raise Exception('Тип переданных данных не совпадает с классом Subject')
    if year is None:
        raise Exception('Объект класса EducationYear не передан')
    elif type(year) != EducationYear:
        raise Exception('Тип переданных данных не совпадает с классом EducationYear')
    if cross_section is None:
        raise Exception('Объект класса CrossSection не передан')
    elif type(cross_section) != CrossSection:
        raise Exception('Тип переданных данных не совпадает с классом CrossSection')
    if points is None:
        raise Exception('Объект класса int не передан')
    elif type(points) != int:
        raise Exception('Тип переданных данных не совпадает с классом int')

    return BRSPoints(student, subject, year, cross_section, points)
