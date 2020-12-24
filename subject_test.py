import unittest
import io
from unittest.mock import patch
from Subject import Subject
from Factory import create_subject
from Main import EditSubject, DeleteSubject


class Subject_TestCase(unittest.TestCase):
    def test_subject(self):
        inputs_subject = Subject(code='Б1.В.01', name='Методы тестирования и верификации программных продуктов')
        self.assertEqual((inputs_subject.code, inputs_subject.name), ('Б1.В.01', 'Методы тестирования и верификации программных продуктов'))

class Create_Subject_TestCase(unittest.TestCase):

    def test_create_subject(self):
        inputs_subject = create_subject('Б1.В.01', 'Методы тестирования и верификации программных продуктов')
        self.assertEqual((inputs_subject.code, inputs_subject.name), ('Б1.В.01', 'Методы тестирования и верификации программных продуктов'))

    def test_create_subject_code1(self):
        inputs_subject = create_subject('Б1.В.01', 'Методы тестирования и верификации программных продуктов')
        self.assertEqual(inputs_subject.code, 'Б1.В.01')

    def test_create_subject_code2(self):
        with self.assertRaises(Exception):
            create_subject('', 'Методы тестирования и верификации программных продуктов')

    def test_create_subject_code3(self):
        with self.assertRaises(Exception):
            create_subject(' ', 'Методы тестирования и верификации программных продуктов')

    def test_create_subject_code4(self):
        with self.assertRaises(Exception):
            create_subject('б1.в.01', 'Методы тестирования и верификации программных продуктов')

    def test_create_subject_name1(self):
        inputs_subject = create_subject('Б1.В.01', 'Методы тестирования и верификации программных продуктов')
        self.assertEqual(inputs_subject.name, 'Методы тестирования и верификации программных продуктов')

    def test_create_student_name2(self):
        with self.assertRaises(Exception):
            create_subject('Б1.В.01', '')

    def test_create_student_name3(self):
        with self.assertRaises(Exception):
            create_subject('Б1.В.01', ' ')

class Main_Subject_TestCase(unittest.TestCase):
    def test_EditSubject(self):
        inputs = ['Б1.В.01']
        with patch('builtins.input', side_effect=inputs) as mock_input:
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                EditSubject()
        result = mock_print.getvalue()
        self.assertEqual('Введите код предмета\nПредмет с таким кодом не найден', result.strip())

    def test_DeleteSubject(self):
        inputs = ['Б1.В.01']
        with patch('builtins.input', side_effect=inputs) as mock_input:
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                DeleteSubject()
        result = mock_print.getvalue()
        self.assertEqual('Введите код предмета\nПредмет с таким кодом не найден', result.strip())



    if __name__ == "__main__":
        unittest.main()
