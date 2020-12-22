import unittest
from Student import Student
from Factory import create_student


class CreateStudentCodeTestCase(unittest.TestCase):
    def test_create_student(self):
        format_name = create_student('1', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                     '89142334939')
        self.assertEqual((format_name.code, format_name.fio, format_name.birthdate, format_name.email,
                          format_name.phone),
                         (1, 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com', '89142334939'))

    def test_create_student_code(self):
        with self.assertRaises(Exception):
            create_student('', 'Федоров Николай Иванович', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_code2(self):
        with self.assertRaises(Exception):
            create_student('abc', 'Федоров Николай Иванович', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')


class StudentTestCase(unittest.TestCase):
    def test_student(self):
        format_name = Student(code=1, fio='Федоров Николай Иванович', birthdate='22.05.1996',
                              email='fednik2011@gmail.com', phone='89142334939')
        self.assertEqual(format_name.fio, 'Федоров Николай Иванович')


if __name__ == "__main__":
    unittest.main()
