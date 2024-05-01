import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsoleCreate(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_no_arguments(self, mock_stdout):
        self.console.do_create('')
        self.assertEqual("** class name missing **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_class(self, mock_stdout):
        self.console.do_create('InvalidClassName')
        self.assertEqual("** class doesn't exist **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_invalid_param_syntax(self, mock_stdout):
        self.console.do_create('State invalid_param')
        self.assertEqual("** invalid parameter syntax **\n", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_valid_params(self, mock_stdout):
        self.console.do_create('State name="California"')
        self.assertTrue(len(storage.all()) > 0)
        # Add more assertions to validate the created instance

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_with_valid_params_file_storage(self, mock_stdout):
        self.console.do_create('State name="California"')
        obj_id = mock_stdout.getvalue().strip()
        obj = storage.all()["State." + obj_id]
        self.assertEqual(obj.name, "California")

    # Add more test cases for different scenarios of object creation


if __name__ == '__main__':
    unittest.main()
