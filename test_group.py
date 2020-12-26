import unittest
import io
from unittest.mock import patch
from Group import Group
from Factory import create_group
from Main import EditGroup, DeleteGroup


class Group_TestCase(unittest.TestCase):
    def test_group(self):
        inputs_group = Group(name='FIIT', year='20')
        self.assertEqual((inputs_group.name, inputs_group.year), ('FIIT', '20'))

class Create_Group_TestCase(unittest.TestCase):

    def test_create_group(self):
        inputs_group = create_group('FIIT', '20')
        self.assertEqual((inputs_group.name, inputs_group.year), ('FIIT', '20'))

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
        self.assertEqual(inputs_group.year, '20')

    def test_create_student_year2(self):
        with self.assertRaises(Exception):
            create_group('FIIT', '')

    def test_create_student_year3(self):
        with self.assertRaises(Exception):
            create_group('FIIT', ' ')

class Main_Group_TestCase(unittest.TestCase):
    def setUp(self):
        self.main_menu_expected = 'FIIT'
        self.main_menu_expected1 = '20' \

    def test_EditGroup(self):
        with patch('builtins.input', side_effect=main_menu_expected+main_menu_expected1) as mock_input:
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                EditGroup()
        result = mock_print.getvalue()
        self.assertEqual('Введите код предмета\nПредмет с таким кодом не найден', result.strip())

    def test_DeleteGroup(self):
        with patch('builtins.input', side_effect=main_menu_expected+main_menu_expected1) as mock_input:
            with patch('sys.stdout', new_callable=io.StringIO) as mock_print:
                DeleteGroup()
        result = mock_print.getvalue()
        self.assertEqual('Введите код предмета\nПредмет с таким кодом не найден', result.strip())



    if __name__ == "__main__":
        unittest.main()
