import unittest
from Factory import create_BRSPoints
from Subject import *
from EducationYear import EducationYear
from Crosssection import CrossSection
from Student import Student
from Group import Group


class CreateBRSPointsTestCase(unittest.TestCase):

    def test_create_brspoints(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual((str(format_name.student.fio) + ", " + str(format_name.subject.name) + ", " + str(
            format_name.year.beginYear) + ", " + str(
            format_name.year.endYear) + ", " + str(format_name.cross_section.name) + ", " + str(format_name.points)),
                         (
                             'Иванов Максим Валерианович, Методы тестирования и верификации программных продуктов, 2020, 2022, Первый к/с, 80'))

    def test_create_brspoints_education_year(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual(str(format_name.year.beginYear) + ', ' + str(format_name.year.endYear), '2020, 2022')

    def test_create_brspoints_education_year1(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, None, cross_section, 80)

    def test_create_brspoints_education_year2(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, ' ', cross_section, 80)

    def test_create_brspoints_education_year3(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, '', cross_section, 80)

    def test_create_brspoints_education_year4(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, 1, cross_section, 80)

    def test_create_brspoints_student(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual(str(format_name.student.fio), 'Иванов Максим Валерианович')

    def test_create_brspoints_student1(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        education_year = EducationYear(2020, 2022)
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(None, subject, education_year, cross_section, 80)

    def test_create_brspoints_student2(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints('', subject, education_year, cross_section, 80)

    def test_create_brspoints_student3(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(' ', subject, education_year, cross_section, 80)

    def test_create_brspoints_student4(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(2, subject, education_year, cross_section, 80)

    def test_create_brspoints_subject(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual(str(format_name.subject.name), 'Методы тестирования и верификации программных продуктов')

    def test_create_brspoints_subject1(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        education_year = EducationYear(2020, 2022)
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(student, None, education_year, cross_section, 80)

    def test_create_brspoints_subject2(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, '', education_year, cross_section, 80)

    def test_create_brspoints_subject3(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, ' ', education_year, cross_section, 80)

    def test_create_brspoints_subject4(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, 1, education_year, cross_section, 80)

    def test_create_brspoints_cross_section(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual(str(format_name.cross_section.name), 'Первый к/с')

    def test_create_brspoints_cross_section1(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        education_year = EducationYear(2020, 2022)
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, None, 80)

    def test_create_brspoints_cross_section2(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, '', 80)

    def test_create_brspoints_cross_section3(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, ' ', 80)

    def test_create_brspoints_cross_section4(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, 1, 80)

    def test_create_brspoints_points(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        education_year = EducationYear(2020, 2022)
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        cross_section = CrossSection('Первый к/с')
        format_name = create_BRSPoints(student, subject, education_year, cross_section, 80)
        self.assertEqual(format_name.points, 80)

    def test_create_brspoints_points1(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        education_year = EducationYear(2020, 2022)
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, cross_section, '80')

    def test_create_brspoints_points2(self):
        student = Student(2, 'Иванов Максим Валерианович', '21.01.1998', 'ivanovmksm98@gmail.com', '89142673402', Group('М-ФИИТ', 20))
        subject = Subject('1', 'Методы тестирования и верификации программных продуктов')
        education_year = EducationYear(2020, 2022)
        cross_section = CrossSection('Первый к/с')
        with self.assertRaises(Exception):
            create_BRSPoints(student, subject, education_year, cross_section, '')
