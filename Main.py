from Crosssection import CrossSection
from EducationYear import EducationYear
from Group import Group
from Subject import Subject

class Main:
    def __init__(self):
        groups=[]
        subjects=[]
        cross_sections=[]
        years=[]
        brs_points=[]
    def PrintGroupMenu(self):
        print("Nothing to do there")
    def PrintSubjectMenu(self):
        print("Nothing to do there")
    def PrintMenu():
        print('''1 - GroupMenu
2 - SubjectMenu''')
        w=int(input())
        if w==1:
                PrintGroupMenu()
        if w==2:
                PrintSubjectMenu()
        else:
                print("error")
    def AddGroup(self):
        pass
    def EditGroup(self):
        pass
    def DeleteGroup(self):
        pass
    def AddStudent(self):
        pass
    def EditStudent(self):
        pass
    def RemoveStudent(self):
        pass
    def AddSubject(self):
        pass
    def EditSubject(self):
        pass
    def DeleteSubject(self):
        pass
    def AddBrsPoint(self):
        pass
    def EditBrsPoint(self):
        pass
    def DeleteBrsPoint(self):
        pass
Main.PrintMenu()