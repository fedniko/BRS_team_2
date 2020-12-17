from Crosssection import CrossSection
from EducationYear import EducationYear
from Group import Group
from Subject import Subject
from Factory import Factory

groups = []
subjects = []
cross_sections = []
years = []
brs_points = []


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
        AddSubject()
    elif w == 2:
        print("===start===")
        for i in subjects:
            print(i.code + ' ' + i.name + '\n')
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


def PrintMenu():
    print('''1 - GroupMenu
2 - SubjectMenu
3 - exit''')
    w = int(input())
    if w == 1:
        PrintGroupMenu()
    elif w == 2:
        PrintSubjectMenu()
    elif w == 3:
        return 0
    else:
        print("error")


def AddGroup():
    pass


def EditGroup():
    pass


def DeleteGroup():
    pass


def AddStudent():
    code = 11
    fio = 'aaa'
    birthdate = '01.01.2020'
    email = 'a@a.ru'
    phone = '1234'
    a = Factory.create_student(code, fio, birthdate, email, phone)
    print(a)


def EditStudent():
    pass


def RemoveStudent():
    pass


def AddSubject():
    pass


def EditSubject():
    pass


def DeleteSubject():
    pass


def AddBrsPoint():
    pass


def EditBrsPoint():
    pass


def DeleteBrsPoint():
    pass


PrintMenu()
