import unittest
import io
from unittest.mock import patch
from Group import Group
from Factory import create_group
from Main import *


class Group_TestCase(unittest.TestCase):
    def test_group(self):
        inputs_group = Group(name='FIIT', year='20')
        self.assertEqual((inputs_group.name, inputs_group.year), ('FIIT', '20'))

class Create_Group_TestCase(unittest.TestCase):

    def test_create_group(self):
        inputs_group = create_group('FIIT', '20')
        self.assertEqual((inputs_group.name, inputs_group.year), ('FIIT', 20))

    def test_create_group_name1(self):
        inputs_group = create_group('FIIT', '20')
        self.assertEqual(inputs_group.name, 'FIIT')

    def test_create_group_name2(self):
        with self.assertRaises(Exception):
            create_group('', '20')

    def test_create_group_name3(self):
        with self.assertRaises(Exception):
            create_group(' ', '20')

    def test_create_group_year1(self):
        inputs_group = create_group('FIIT', '20')
        self.assertEqual(inputs_group.year, 20)

    def test_create_student_year2(self):
        with self.assertRaises(Exception):
            create_group('FIIT', '')

    def test_create_student_year3(self):
        with self.assertRaises(Exception):
            create_group('FIIT', ' ')

    def test_create_student_year3(self):
        with self.assertRaises(Exception):
            create_group('FIIT', 'FIIT')

class MainStudentTestCase(unittest.TestCase):
    def setUp(self):
        self.main_menu_expected3 = 'Введите название группы\nВведите год группы\nЧто нужно редактировать? ' \
                                   '\n1 Название группы \n2 Год группы\nВведите год\nГод группы изменился!'
        self.main_menu_expected1 = 'Введите название группы\nВведите год группы\nГруппа создана!'
        self.main_menu_expected2 = 'Введите название группы\nВведите год группы\nГруппа удалена!'

        self.user_menu_inpute1 = ['FIIT', '21' , '5', '5']
        self.user_menu_input1 = ['IVT', '21','5' ,'5']
        self.user_menu_input2 = ['FIIT', '20', '1','21', '5', '5']

        x = create_group('FIIT', '20')
        groups.append(x)
        x = create_group('IVT', '21')
        groups.append(x)
        x = create_group('MAG', '19')
        groups.append(x)


    @patch('sys.stdout', new_callable=io.StringIO)
    def test_AddGroup(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_inpute1):
            AddGroup()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected1, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_DeleteGroup(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input1):
            DeleteGroup()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected2, result)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_EditGroup(self, mock_obj):
        with patch('builtins.input', side_effect=self.user_menu_input2):
            EditGroup()
        result = mock_obj.getvalue().strip()
        self.assertEqual(self.main_menu_expected3, result)


if __name__ == "__main__":
    unittest.main()