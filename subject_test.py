import unittest
import io
from unittest.mock import patch
from Subject import Subject
from Factory import create_subject
from Main import *

#ТестSubject
class Subject_TestCase(unittest.TestCase):
    def test_subject(self):
        inputs_subject = Subject(code='Б1.В.01', name='Методы тестирования и верификации программных продуктов')
        self.assertEqual((inputs_subject.code, inputs_subject.name), ('Б1.В.01', 'Методы тестирования и верификации программных продуктов'))

#FactoryCreate_Subject
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

#Main_Add_Subject

class Main_Add_Subject_TestCase(unittest.TestCase):
    def setUp(self):
        self.add_subject_menu_expected1 = 'Введите код предмета\nВведите название предмета\nПредмет создан'
        self.add_subject_menu_expected2 = 'Введите код предмета\nПредмет с таким кодом уже существует'
        self.user_menu_input1 = ['Б1.В.58']
        self.user_menu_input2 = ['Научно исследовательский семинар']
        self.user_menu_input3 = ['Б1.О.09']
        x = create_subject('Б1.О.09', 'Разработка приложений на языке Python')
        subjects.append(x)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_subject_menu_expected1(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1+self.user_menu_input2):
            AddSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.add_subject_menu_expected1, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_subject_menu_expected2(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input3):
            AddSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.add_subject_menu_expected2, result)


#Main_Edit_Subject

class Main_Edit_Subject_TestCase(unittest.TestCase):
    def setUp(self):
        self.edit_subject_menu_expected1 = 'Введите код предмета\nПредмет с таким кодом не найден'
        self.edit_subject_menu_expected2 = 'Введите код предмета\n' \
                                           'Что хотите изменить?\n' \
                                           '1 Код\n2 Название\n3 Назад\n' \
                                           'Введите новое название предмета\n' \
                                           'Успешно изменено'
        self.edit_subject_menu_expected3 = 'Введите код предмета\n' \
                                           'Что хотите изменить?\n' \
                                           '1 Код\n2 Название\n3 Назад\n' \
                                           'Введите новый код предмета\n' \
                                           'Успешно изменено'
        self.user_menu_input1 = ['Б2.Г.87']
        self.user_menu_input2 = ['Python']
        self.user_menu_input3 = ['Б1.О.09']
        self.user_menu_input4 = ['Б1.О.10']
        x = create_subject('Б1.О.09', 'Разработка приложений на языке Python')
        subjects.append(x)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_subject_menu_expected1(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1):
            EditSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.edit_subject_menu_expected1, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_subject_menu_expected2(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input3+[2]+self.user_menu_input2):
            EditSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.edit_subject_menu_expected2, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_edit_subject_menu_expected3(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input3+[1]+self.user_menu_input4):
            EditSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.edit_subject_menu_expected3, result)


#Main_Delete_Subject

class Main_Delete_Subject_TestCase(unittest.TestCase):
    def setUp(self):
        self.delete_subject_menu_expected1 = 'Введите код предмета\nПредмет с таким кодом не найден'
        self.delete_subject_menu_expected2 = 'Введите код предмета\nПредмет успешно удален'

        self.user_menu_input1 = ['Б2.O.55']
        self.user_menu_input2 = ['Б1.О.09']
        x = create_subject('Б1.О.09', 'Разработка приложений на языке Python')
        subjects.append(x)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_subject_menu_expected1(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1):
            DeleteSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.delete_subject_menu_expected1, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_delete_subject_menu_expected2(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input2):
            DeleteSubject()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.delete_subject_menu_expected2, result)


    if __name__ == "__main__":
        unittest.main()
