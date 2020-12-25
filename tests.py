import unittest
import io
from unittest.mock import patch
from Student import Student
from Factory import create_student
from Main import EditStudent, RemoveStudent


class CreateStudentTestCase(unittest.TestCase):
    def test_create_student(self):
        format_name = create_student('1', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                     '89142334939')
        self.assertEqual((format_name.code, format_name.fio, format_name.birthdate, format_name.email,
                          format_name.phone),
                         (1, 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com', '89142334939'))

    def test_create_student_code(self):
        format_name = create_student('1', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                     '89142334939')
        self.assertEqual(format_name.code, 1)

    def test_create_student_code2(self):
        with self.assertRaises(Exception):
            create_student('', 'Федоров Николай Иванович', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_code3(self):
        with self.assertRaises(Exception):
            create_student('abc', 'Федоров Николай Иванович', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_fio(self):
        format_name = create_student('1', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                     '89142334939')
        self.assertEqual(format_name.fio, 'Федоров Николай Иванович')

    def test_create_student_fio2(self):
        with self.assertRaises(Exception):
            create_student('1', '', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_fio3(self):
        with self.assertRaises(Exception):
            create_student('1', ' ', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_fio4(self):
        with self.assertRaises(Exception):
            create_student('1', 'Николай', '22.05.1996',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_birthdate(self):
        format_name = create_student('1', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                     '89142334939')
        self.assertEqual(format_name.birthdate, '22.05.1996')

    def test_create_student_birthdate2(self):
        with self.assertRaises(Exception):
            create_student('1', 'Федоров Николай Иванович', '',
                           'fednik2011@gmail.com', '89142334939')

    def test_create_student_birthdate3(self):
        with self.assertRaises(ValueError):
            create_student('1', 'Федоров Николай Иванович', '22.05.96',
                           'fednik2011@gmail.com', '89142334939')


class MainStudentTestCase(unittest.TestCase):
    def test_EditStudent(self):
        inputs = [1]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                EditStudent()
        result = mock_print.getvalue()
        self.assertEqual('Введите код студента\nСтудент с таким кодом не найден', result.strip())

    def test_RemoveStudent(self):
        inputs = [1]
        with patch('builtins.input', side_effect=inputs):
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                RemoveStudent()
        result = mock_print.getvalue()
        self.assertEqual('Введите код студента\nСтудент с таким кодом не найден', result.strip())


class StudentTestCase(unittest.TestCase):
    def test_student(self):
        format_name = Student(code=1, fio='Федоров Николай Иванович', birthdate='22.05.1996',
                              email='fednik2011@gmail.com', phone='89142334939')
        self.assertEqual(format_name.fio, 'Федоров Николай Иванович')


if __name__ == "__main__":
    unittest.main()
