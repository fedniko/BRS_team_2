import io
import unittest
from unittest.mock import patch
from Main import PrintMenu, PrintGroupMenu, PrintSubjectMenu, groups, subjects
from Group import Group
from Subject import Subject
from Crosssection import CrossSection
from EducationYear import EducationYear

class Crosssection_Tests(unittest.TestCase):
    def test_testcase1(self):
        dg=CrossSection("FIIT")
        self.assertEqual("FIIT", dg.name)


class EducationYear_Tests(unittest.TestCase):
    def test_testcase1(self):
        sg=EducationYear(25,26)
        self.assertEqual([25,26], [sg.beginYear,sg.endYear])

dg=Group("FIIT",20)
groups.append(dg)
sg=Subject(25,"Algebra")
subjects.append(sg)
MainMenu_e="1 - GroupMenu\n2 - SubjectMenu\n3 - StudentMenu\n4 - BRSMenu\n5 - exit"
GroupMenu_e='1 Создать новую группу \n2 Показать все созданные группы \n3 Удалить группу \n4 Изменить группу \n5 Назад'
SubjectMenu_e='1 create a new subject\n2 show all created subjects\n3 delete Subject\n4 edit subject\n5 go back'
error_e='error'

class PrintMenu_tests(unittest.TestCase):

    def test_testcase0(self):
        find = 0
        for i in subjects:
            if i.code == 25:
                find = 1
        self.assertEqual(1, find)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase1(self, mock_obj):
        input = ['2','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e+'\n'+SubjectMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase2(self, mock_obj):
        input = ['7','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e+'\n'+error_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase3(self, mock_obj):
        input = ['kjojih','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e+'\n'+error_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase4(self, mock_obj):
        input = ['-7','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e+'\n'+error_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase5(self, mock_obj):
        input = ['5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase6(self, mock_obj):
        input = ['1','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintMenu()
        result = mock_obj.getvalue()
        self.assertEqual(MainMenu_e+'\n'+GroupMenu_e+'\n'+MainMenu_e, result.strip())

class PrintGroupMenu_tests(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase1(self, mock_obj):
        input = ['53','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintGroupMenu()
        result = mock_obj.getvalue()
        self.assertEqual(GroupMenu_e+'\n'+error_e+'\n'+GroupMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase2(self, mock_obj):
        input = ['hugyhf','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintGroupMenu()
        result = mock_obj.getvalue()
        self.assertEqual(GroupMenu_e+'\n'+error_e+'\n'+GroupMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase3(self, mock_obj):
        input = ['5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintGroupMenu()
        result = mock_obj.getvalue()
        self.assertEqual(GroupMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase4(self, mock_obj):
        input = ['0','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintGroupMenu()
        result = mock_obj.getvalue()
        self.assertEqual(GroupMenu_e+'\n'+error_e+'\n'+GroupMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase5(self, mock_obj):
        input = ['2','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintGroupMenu()
        result = mock_obj.getvalue()
        self.assertEqual(GroupMenu_e+'\n'+'===start===\nГруппа: FIIT-20\n\n===end===\n'+GroupMenu_e+'\n'+MainMenu_e, result.strip())

class PrintSubjectMenu_tests(unittest.TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase2(self, mock_obj):
        input = ['53','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintSubjectMenu()
        result = mock_obj.getvalue()
        self.assertEqual(SubjectMenu_e+'\n'+error_e+'\n'+SubjectMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase3(self, mock_obj):
        input = ['hugyhf','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintSubjectMenu()
        result = mock_obj.getvalue()
        self.assertEqual(SubjectMenu_e+'\n'+error_e+'\n'+SubjectMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase4(self, mock_obj):
        input = ['5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintSubjectMenu()
        result = mock_obj.getvalue()
        self.assertEqual(SubjectMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase5(self, mock_obj):
        input = ['0','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintSubjectMenu()
        result = mock_obj.getvalue()
        self.assertEqual(SubjectMenu_e+'\n'+error_e+'\n'+SubjectMenu_e+'\n'+MainMenu_e, result.strip())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_testcase6(self, mock_obj):
        input = ['2','5','5']
        with patch('builtins.input', side_effect=input) as mock_input:
             PrintSubjectMenu()
        result = mock_obj.getvalue()
        self.assertEqual(SubjectMenu_e+'\n'+'===start===\nКод: 25 Предмет: Algebra\n\n===end===\n'+SubjectMenu_e+'\n'+MainMenu_e, result.strip())

if __name__ == '__main__':
    unittest.main()