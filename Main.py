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
    w = input()
    if w == "1":
        AddGroup()
    elif w == "2":
        print("===start===")
        for i in groups:
            print(str(i.name) + ' ' + str(i.year) + '\n')
        print("===end===")
        PrintGroupMenu()
    elif w == "3":
        DeleteGroup()
    elif w == "4":
        EditGroup()
    elif w == "5":
        PrintMenu()
    else:
        print("error")
        PrintGroupMenu()


def PrintSubjectMenu():
    print("1 create a new subject\n2 show all created subjects\n3 delete Subject\n4 edit subject\n5 go back")
    w = input()
    if w == "1":
        AddSubject()
    elif w == "2":
        print("===start===")
        for i in subjects:
            print(str(i) + '\n')
        print("===end===")
        PrintSubjectMenu()
    elif w == "3":
        DeleteSubject()
    elif w == "4":
        EditSubject()
    elif w == "5":
        PrintMenu()
    else:
        print("error")
        PrintSubjectMenu()


def PrintStudentMenu():
    print('1 Создать нового студента\n2 Показать всех студентов\n3 Удалить студента\n'
          '4 Редактировать даннные студента\n5 Назад')
    w = input()
    if w == "1":
        AddStudent()
    elif w == "2":
        print("===start===")
        for i in students:
            print(str(i) + '\n')
        print("===end===")
        PrintStudentMenu()
    elif w == "3":
        RemoveStudent()
    elif w == "4":
        EditStudent()
    elif w == "5":
        PrintMenu()
    else:
        print("error")
        PrintStudentMenu()


def PrintBRSMenu():
    print("1 create a new BRS point\n2 show all created BRS point\n3 remove BRS point\n4 edit BRS point\n5 go back")
    w = input()
    if w == "1":
        AddBrsPoint()
    elif w == "2":
        print("===start===")
        for i in brs_points:
            print(str(i) + '\n')
        print("===end===")
        PrintBRSMenu()
    elif w == "3":
        DeleteBrsPoint()
    elif w == "4":
        EditBrsPoint()
    elif w == "5":
        PrintMenu()
    else:
        print("error")
        PrintBRSMenu()


def PrintMenu():
    print("1 - GroupMenu\n2 - SubjectMenu\n3 - StudentMenu\n4 - BRSMenu\n5 - exit")
    w = input()
    if w == "1":
        PrintGroupMenu()
    elif w == "2":
        PrintSubjectMenu()
    elif w == "3":
        PrintStudentMenu()
    elif w == "4":
        PrintBRSMenu()
    elif w == "5":
        return 0
    else:
        print("error")
        PrintMenu()


def AddGroup():
    print('Enter group name')
    name = str(input())
    print('Enter Group year')
    year = str(input())
    for i in groups:
        if i.name == name and i.year == year:
            print("This group already exists!")
            if __name__ == '__main__':
                PrintGroupMenu()
    else:
        x = create_group(name, year)
        groups.append(x)
        print('Group created')
    if __name__ == '__main__':
        PrintGroupMenu()


def EditGroup():
    print('Enter group name')
    name = str(input())
    print('Enter Group year')
    year = str(input())
    for i in groups:
        if i.name == name and i.year == year:
            print("What need to edit?\n1 year\n2 name")
            w = input()
            if w == "1":
                print("enter year")
                year = str(input())
                for j in groups:
                    if i.name == name and i.year == year:
                        print("The group with this year and name already exists. Try again")
                        if __name__ == '__main__':
                            PrintGroupMenu()
                        break
                else:
                    i.name = name
                    i.year = year
                    print("Group year changed!")
                    if __name__ == '__main__':
                        PrintGroupMenu()
                    break
            elif w == "2":
                print("enter name")
                name = str(input())
                i.name = name
                print("Group name changed!")
                PrintGroupMenu()
    else:
        print("This group not exist!")
    if __name__ == '__main__':
        PrintGroupMenu()


def DeleteGroup():
    print('Enter group name')
    name = str(input())
    print('Enter Group year')
    year = str(input())
    for i in groups:
        if i.name == name and i.year == year:
            groups.remove(i)
            print('Group deleted')
            if __name__ == '__main__':
                PrintGroupMenu()
            break
    else:
        print("This group not exist!")
        PrintGroupMenu()
    if __name__ == '__main__':
        PrintGroupMenu()


def AddStudent():
    print('Введите код студента')
    code = str(input())
    for i in students:
        if i.code == int(code):
            print('Студент с таким кодом уже существует')
            if __name__ == '__main__':
                PrintStudentMenu()
            break
    else:
        print('Введите ФИО студента')
        fio = str(input())
        print('Введите дату рождения студента в формате ДД.ММ.ГГГГ')
        birthdate = str(input())
        print('Введите email студента')
        email = str(input())
        print('Введите телефон студента')
        phone = str(input())
        print('Введите название группы студента')
        grno = input()
        print('Введите год группы студента')
        grgo = int(input())
        for j in groups:
            if j.name == grno and j.year == grgo:
                try:
                    x = create_student(code, fio, birthdate, email, phone, j)
                    students.append(x)
                    print('Студент успешно создан')
                except Exception:
                    print('Ошибка')
        else:
            print('Группа не найдена')
    if __name__ == '__main__':
        PrintStudentMenu()


def EditStudent():
    # Создание для теста
    # x = create_student('9696', 'Иванов Иван', '01.01.2001', 'a@gmal.com', '89241234567')
    # students.append(x)
    #
    # x = create_student('1414', 'Иванов Иван', '01.01.2001', 'a@gmal.com', '89241234567')
    # students.append(x)
    #
    print('Введите код студента')
    a = int(input())
    for i in students:
        if i.code == a:
            print('Что хотите изменить?')
            print("1 Код\n2 ФИО\n3 Дата рождения\n4 Почта\n5 Телефон\n6 Назад")
            w = input()
            if w == "1":
                print('Введите новый код студента')
                new_code = (int(input()))
                for u in students:
                    if u.code == new_code:
                        print("Студент с таким кодом уже существует")
                        if __name__ == '__main__':
                            PrintStudentMenu()
                        break
                else:
                    i.code = new_code
                    print('Успешно изменено')
            elif w == "2":
                print('Введите новое ФИО студента')
                i.fio = (str(input()))
                print('Успешно изменено')
            elif w == "3":
                print('Введите новую дату рождения студента')
                i.birthdate = (str(input()))
                print('Успешно изменено')
            elif w == "4":
                print('Введите новую почту студента')
                i.email = (str(input()))
                print('Успешно изменено')
            elif w == "5":
                print('Введите новый телефон студента')
                i.phone = (str(input()))
                print('Успешно изменено')
            elif w == "6":
                print('Введите новое название группы студента')
                grno = input()
                print('Введите новый год группы студента')
                grgo = int(input())
                for u in groups:
                    if u.name == grno and u.year == grgo:
                        i.group = u
                        print('Успешно изменено')
                else:
                    print('Группа не найдена')
            elif w == "7":
                PrintStudentMenu()
            else:
                print("error")
                if __name__ == '__main__':
                    PrintStudentMenu()
            if __name__ == '__main__':
                PrintStudentMenu()
            break
    else:
        print('Студент с таким кодом не найден')
    if __name__ == '__main__':
        PrintStudentMenu()


def RemoveStudent():
    # Создание для теста
    # x = create_student('6969', 'Иванов Иван', '01.01.2001', 'a@gmal.com', '89241234567')
    # students.append(x)
    #
    print('Введите код студента')
    x = int(input())
    for i in students:
        if i.code == x:
            students.remove(i)
            print('Студент успешно удален')
            if __name__ == '__main__':
                PrintStudentMenu()
            break
    else:
        print('Студент с таким кодом не найден')
    if __name__ == '__main__':
        PrintStudentMenu()


def AddSubject():
    print('Введите код предмета')
    a = str(input())
    for i in subjects:
        if i.code == a:
            print("Предмет с таким кодом уже существует")
            if __name__ == '__main__':
                PrintSubjectMenu()
            break
    else:
        print('Введите название предмета')
        name = str(input())
        try:
            subjects.append(create_subject(a, name))
            print('Предмет создан')
        except Exception:
            print('Код предмета должен содержать только заглавные буквы, цифры и не должен быть пустым')

    if __name__ == '__main__':
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
                print('Успешно изменено')
            elif w == 2:
                print('Введите новое название предмета')
                i.name = (str(input()))
                print('Успешно изменено')
            elif w == 3:
                PrintSubjectMenu()
            else:
                print("error")
                if __name__ == '__main__':
                    PrintSubjectMenu()
            if __name__ == '__main__':
                PrintSubjectMenu()
            break
    else:
        print('Предмет с таким кодом не найден')
        if __name__ == '__main__':
            PrintSubjectMenu()


def DeleteSubject():
    print('Введите код предмета')
    x = str(input())
    for i in subjects:
        if i.code == x:
            subjects.remove(i)
            print('Предмет успешно удален')
            if __name__ == '__main__':
                PrintSubjectMenu()
            break
    else:
        print('Предмет с таким кодом не найден')
        if __name__ == '__main__':
            PrintSubjectMenu()


def AddBrsPoint():
    print('Enter crossection')
    cross = str(input())
    print('Enter subject code')
    scode = str(input())
    for i in subjects:
        if i.code == scode:
            print('Enter code student')
            stcode = int(input())
            for ist in students:
                if ist.code == stcode:
                    print('Enter eduyear\nbegin')
                    beg = int(input())
                    print('end')
                    end = int(input())
                    for j in brs_points:
                        if j.student.code == stcode and j.subject.code == scode and j.cross_section.name == cross and j.year.beginYear == beg and j.year.endYear == end:
                            print("This BRS point already exists!")
                            PrintBRSMenu()
                    else:
                        print("Enter BRS point")
                        point = int(input())
                        x = create_BRSPoints(ist, i, EducationYear(beg, end), CrossSection(cross), point)
                        brs_points.append(x)
                        print('BRS Point created')
                else:
                    print('Student not found')
                    PrintBRSMenu()
        else:
            print("Subject not found")
            PrintBRSMenu()
    if __name__ == '__main__':
        PrintBRSMenu()


def EditBrsPoint():
    print('Enter crossection')
    cross = str(input())
    print('Enter subject code')
    scode = str(input())
    for i in subjects:
        if i.code == scode:
            print('Enter code student')
            stcode = int(input())
            for ist in students:
                if ist.code == stcode:
                    print('Enter eduyear\nbegin')
                    beg = int(input())
                    print('end')
                    end = int(input())
                    for j in brs_points:
                        if j.student.code == stcode and j.subject.code == scode and j.cross_section.name == cross and j.year.beginYear == beg and j.year.endYear == end:
                            print("1 edit subject code\n2 crosssection\n3 begin year\n4 end year\n5 point")
                            inw = input()
                            if inw == "1":
                                print("enter subject code")
                                scode = int(input())
                                for u in subjects:
                                    if u.code == scode:
                                        j.subject.code = scode
                                else:
                                    print("subject not found")
                            elif inw == "2":
                                print("enter crosssection")
                                cross = str(input())
                                j.cross_section.name = cross
                            elif inw == "3":
                                print('Enter begin year')
                                beg = int(input())
                                j.year.beginYear = beg
                            elif inw == "4":
                                print('Enter end year')
                                end = int(input())
                                j.year.endYear = end
                            elif inw == "5":
                                print("enter point")
                                point = int(input())
                                j.points = point
                            else:
                                print("error")
                else:
                    print("BRS point not found")
        else:
            print("Subject not found")
            PrintBRSMenu()
    if __name__ == '__main__':
        PrintBRSMenu()


def DeleteBrsPoint():
    print('Enter crossection')
    cross = str(input())
    print('Enter subject code')
    scode = str(input())
    for i in subjects:
        if i.code == scode:
            print('Enter code student')
            stcode = int(input())
            for ist in students:
                if ist.code == stcode:
                    print('Enter eduyear\nbegin')
                    beg = int(input())
                    print('end')
                    end = int(input())
                    for j in brs_points:
                        if j.student.code == stcode and j.subject.code == scode and j.cross_section.name == cross and j.year.beginYear == beg and j.year.endYear == end:
                            brs_points.remove(j)
                            print("BRS deleted")
                            PrintBRSMenu()
                    else:
                        print("BRS point not found")
        else:
            print("Subject not found")
            PrintBRSMenu()
    if __name__ == '__main__':
        PrintBRSMenu()


if __name__ == '__main__':
    PrintMenu()
