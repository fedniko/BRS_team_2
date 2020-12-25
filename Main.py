from Crosssection import CrossSection
from EducationYear import EducationYear
from Group import Group
from Subject import Subject
from Factory import *
from Student import Student

groups = []
subjects = []
cross_sections = []
years = []
brs_points = []
students = []


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
        PrintGroupMenu()


def PrintSubjectMenu():
    print("1 create a new subject\n2 show all created subjects\n3 delete Subject\n4 edit subject\n5 go back")
    w = int(input())
    if w == 1:
        print('Введите код предмета')
        AddSubject(str(input()))
    elif w == 2:
        print("===start===")
        for i in subjects:
            print(str(i)+'\n')
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
        PrintSubjectMenu()


def PrintStudentMenu():
    print('1 Создать нового студента\n2 Показать всех студентов\n3 Удалить студента\n'
          '4 Редактировать даннные студента\n5 Назад')
    w = int(input())
    if w == 1:
        print('Введите код студента')
        AddStudent(str(input()))
    elif w == 2:
        print("===start===")
        for i in students:
            print(str(i)+'\n')
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
        PrintStudentMenu()


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
        PrintMenu()


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
    x = create_student(code, fio, birthdate, email, phone)
    students.append(x)
    print('Студент создан/изменен')
    PrintStudentMenu()


def EditStudent():
    print('Введите код студента')
    a = int(input())
    for i in students:
        if i.code == a:
            print('Что хотите изменить?')
            print("1 Код\n2 ФИО\n3 Дата рождения\n4 Почта\n5 Телефон\n6 Назад")
            w = int(input())
            if w == 1:
                print('Введите новый код студента')
                i.code = (int(input()))
            elif w == 2:
                print('Введите новое ФИО студента')
                i.fio = (str(input()))
            elif w == 3:
                print('Введите новую дату рождения студента')
                i.birthdate = (str(input()))
            elif w == 4:
                print('Введите новую почту студента')
                i.email = (str(input()))
            elif w == 5:
                print('Введите новый телефон студента')
                i.phone = (str(input()))
            elif w == 5:
                PrintStudentMenu()
            else:
                print("error")
                PrintStudentMenu()
            PrintStudentMenu()
    else:
        print('Студент с таким кодом не найден')
        # PrintStudentMenu()


def RemoveStudent():
    print('Введите код студента')
    x = int(input())
    for i in students:
        if i.code == x:
            students.remove(i)
            print('Студент успешно удален')
            PrintStudentMenu()
    else:
        print('Студент с таким кодом не найден')
        # PrintStudentMenu()


def AddSubject(a):
    code = a
    print('Введите название предмета')
    name = str(input())
    x = create_subject(code, name)
    subjects.append(x)
    print('Предмет создан')
    PrintSubjectMenu()


def EditSubject():
    print('Введите код предмета')
    a = str(input())
    for i in subjects:
        if i.code == a:
            print('Что хотите изменить?')
            print("1 Код\n2 Название\n3 Назад")
            w = int(input())
            if w == 1:
                print('Введите новый код предмета')
                i.code = (str(input()))
            elif w == 2:
                print('Введите новое название предмета')
                i.name = (str(input()))
            elif w == 3:
                PrintSubjectMenu()
            else:
                print("error")
                PrintSubjectMenu()
            PrintSubjectMenu()
    else:
        print('Предмет с таким кодом не найден')
        PrintSubjectMenu()


def DeleteSubject():
    print('Введите код предмета')
    x = str(input())
    for i in subjects:
        if i.code == x:
            subjects.remove(i)
            print('Предмет успешно удален')
            PrintSubjectMenu()
    else:
        print('Предмет с таким кодом не найден')
        PrintSubjectMenu()


def AddBrsPoint():
    pass


def EditBrsPoint():
    pass


def DeleteBrsPoint():
    pass


if __name__ == '__main__':
    PrintMenu()