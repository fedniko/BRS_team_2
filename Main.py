from Crosssection import CrossSection
from EducationYear import EducationYear
from Group import Group
from Subject import Subject
from Factory import *
from Student import Student

groups = []
subjects = {}
cross_sections = []
years = []
brs_points = []
students = {}


def PrintGroupMenu():
    print("1 create a new Group\n2 show all created groups\n3 delete group\n4 edit group\n5 go back")
    w = int(input())
    if w == 1:
        AddGroup()
    elif w == 2:
        print("===start===")
        for i in groups:
            print(i.year + ' ' + i.name + '\n')
        print("===end===")
        PrintGroupMenu()
    elif w == 3:
        DeleteGroup()
    elif w == 4:
        EditGroup()
    elif w == 5:
        PrintMenu()
    else:
        print("error")


def PrintSubjectMenu():
    print("1 create a new subject\n2 show all created subjects\n3 delete Subject\n4 edit subject\n5 go back")
    w = int(input())
    if w == 1:
        print('Введите код предмета')
        AddSubject(str(input()))
    elif w == 2:
        print("===start===")
        for i in subjects:
            print(subjects)
        print("===end===")
        PrintSubjectMenu()
    elif w == 3:
        DeleteSubject()
    elif w == 4:
        EditSubject()
    elif w == 5:
        PrintMenu()
    else:
        print("error")


def PrintStudentMenu():
    print("1 create a new Student\n2 show all created students\n3 remove student\n4 edit student\n5 go back")
    w = int(input())
    if w == 1:
        print('Введите код студента')
        AddStudent(str(input()))
    elif w == 2:
        print("===start===")
        print(students)
        print("===end===")
        PrintStudentMenu()
    elif w == 3:
        RemoveStudent()
    elif w == 4:
        EditStudent()
    elif w == 5:
        PrintMenu()
    else:
        print("error")


def PrintMenu():
    print('''1 - GroupMenu
2 - SubjectMenu
3 - StudentMenu
4 - exit''')
    w = int(input())
    if w == 1:
        PrintGroupMenu()
    elif w == 2:
        PrintSubjectMenu()
    elif w == 3:
        PrintStudentMenu()
    elif w == 4:
        return 0
    else:
        print("error")


def AddGroup():
    pass


def EditGroup():
    pass


def DeleteGroup():
    pass


def AddStudent(a):
    code = a
    print('Введите ФИО студента')
    fio = str(input())
    print('Введите дату рождения студента в формате ДД.ММ.ГГГГ')
    birthdate = str(input())
    print('Введите email студента')
    email = str(input())
    print('Введите телефон студента')
    phone = str(input())
    create_student(code, fio, birthdate, email, phone)
    students[int(code)] = fio, birthdate, email, phone
    print('Студент создан/изменен')
    PrintStudentMenu()


def EditStudent():
    print('Введите код студента')
    a = int(input())
    try:
        print(students.pop(a))
        AddStudent(a)
    except KeyError:
        print('Студент с таким кодом не найден')
        # PrintStudentMenu()


def RemoveStudent():
    print('Введите код студента')
    try:
        print(students.pop(int(input())))
        print('Студент успешно удален')
        PrintStudentMenu()
    except KeyError:
        print('Студент с таким кодом не найден')
        # PrintStudentMenu()


def AddSubject(a):
    code = a
    print('Введите название предмета')
    name = str(input())
    create_subject(code, name)
    subjects[str(input(code))] = name
    print('Предмет создан')
    PrintSubjectMenu()


def EditSubject():
    print('Введите код предмета')
    a = str(input())
    try:
        print(subjects.pop(a))
        AddSubject(a)
    except KeyError:
        print('Предмет с таким кодом не найден')
        #PrintSubjectMenu()


def DeleteSubject():
    print('Введите код предмета')
    try:
        print(subjects.pop(str(input())))
        print('Предмет успешно удален')
        PrintSubjectMenu()
    except KeyError:
        print('Предмет с таким кодом не найден')
        #PrintSubjectMenu()


def AddBrsPoint():
    pass


def EditBrsPoint():
    pass


def DeleteBrsPoint():
    pass


if __name__ == '__main__':
    PrintMenu()