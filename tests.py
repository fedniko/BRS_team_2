import unittest
import io
from unittest.mock import patch
from Student import Student
from Factory import create_student
from Main import EditStudent, RemoveStudent, AddStudent, PrintStudentMenu


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
    def setUp(self):
        self.main_menu_expected = 'Введите код студента\nСтудент с таким кодом не найден'
        self.main_menu_expected1 = 'Введите код студента\nВведите ФИО студента\n' \
                                   'Введите дату рождения студента в формате ДД.ММ.ГГГГ\nВведите email студента\n' \
                                   'Введите телефон студента\nСтудент успешно создан'
        self.main_menu_expected2 = 'Введите код студента\nСтудент успешно удален'
        self.main_menu_expected3 = 'Введите код студента\nЧто хотите изменить?\n1 Код\n2 ФИО\n3 Дата рождения\n' \
                                   '4 Почта\n5 Телефон\n6 Назад\nВведите новое ФИО студента\nУспешно изменено'
        self.user_menu_input = [1]
        self.user_menu_input1 = ['2', 'Федоров Николай Иванович', '22.05.1996', 'fednik2011@gmail.com',
                                 '89142334939']
        self.user_menu_input2 = ['Алексеев Алексей Алексеевич']

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_EditStudentError(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input):
            EditStudent()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_RemoveStudentError(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input):
            RemoveStudent()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_AddStudent(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1):
            AddStudent()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected1, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_RemoveStudent(self, mock_obj):
        with patch('builtins.input', side_effect=[6969]):
            RemoveStudent()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected2, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_EditStudent(self, mock_obj):
        with patch('builtins.input', side_effect=[9696]+[2]+self.user_menu_input2):
            EditStudent()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected3, result)


class StudentTestCase(unittest.TestCase):
    def test_student(self):
        format_name = Student(code=1, fio='Федоров Николай Иванович', birthdate='22.05.1996',
                              email='fednik2011@gmail.com', phone='89142334939')
        self.assertEqual(format_name.fio, 'Федоров Николай Иванович')


if __name__ == "__main__":
    unittest.main()
