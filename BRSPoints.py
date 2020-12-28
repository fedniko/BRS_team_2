from EducationYear import EducationYear
from Subject import Subject
from Crosssection import CrossSection
from Student import Student


class BRSPoints:
    def __init__(self, student: Student, subject: Subject, year: EducationYear, cross_section: CrossSection, points: int):
        self.student = student
        self.subject = subject
        self.year = year
        self.cross_section = cross_section
        self.points = points

    def __str__(self):
        template = 'Student: {} Subject: {} Year: {} Srez: {} Points: {}'
        return template.format(self.student.fio + ' - ' + str(self.student.group), self.subject.name, str(self.year.beginYear) + '-' + str(self.year.endYear),
                               self.cross_section.name, self.points)
