from EducationYear import EducationYear
from Subject import Subject
from Crosssection import CrossSection


class BRSPoints:
    def __init__(self, subject: Subject,year: EducationYear, cross_section: CrossSection, points: int):
        self.subject = subject
        self.year = year
        self.cross_section = cross_section
        self.points = points

    def __str__(self):
        template = 'Предмет: {} Год: {} Срез: {} Баллы: {}'
        return template.format(self.subject.name, str(self.year.beginYear)+'-'+str(self.year.endYear), self.cross_section.name, self.points, 