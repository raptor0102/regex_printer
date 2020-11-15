import unittest
from src.RegexPrinter import *
import contextlib
from io import StringIO
from tests.test_the_output_no_color import DummyNameClass


class TestRegexMachine(unittest.TestCase):

    def test_no_output(self):
        dummy_obj = DummyNameClass(input_file='/project/tests/dummy_input1.txt')
        regex_object = RegexPrinterMachine(regex='kukukuku', full_files_path=[dummy_obj])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            regex_object.print()
        output = temp_stdout.getvalue().strip()
        self.assertEqual(output, "")

    def test_full_line_match(self):
        dummy_obj = DummyNameClass(input_file='/project/tests/dummy_input2.txt')
        regex_object = RegexPrinterMachine(regex='[2-6]', full_files_path=[dummy_obj])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            regex_object.print()
        output = temp_stdout.getvalue().strip()
        with open('/project/tests/dummy_output2_machine.txt') as fp:
            output_result = fp.read()

        self.assertEqual(output, output_result)

    def test_special_chars(self):
        dummy_obj = DummyNameClass(
            input_file='/project/tests/dummy_input3.txt')
        regex_object = RegexPrinterMachine(regex='{', full_files_path=[dummy_obj])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            regex_object.print()
        output = temp_stdout.getvalue().strip()
        with open('/project/tests/dummy_output3_machine.txt') as fp:
            output_result = fp.read()
        self.assertEqual(output, output_result)

    def test_single_line_numbers(self):
        dummy_obj = DummyNameClass(
            input_file='/project/tests/dummy_input4.txt')
        regex_object = RegexPrinterMachine(regex='[0-9][0-9]+', full_files_path=[dummy_obj])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            regex_object.print()
        output = temp_stdout.getvalue().strip()
        with open('/project/tests/dummy_output4_machine.txt') as fp:
            output_result = fp.read()
        self.assertEqual(output, output_result)

    def test_simple_text(self):
        dummy_obj = DummyNameClass(
            input_file='/project/tests/dummy_input1.txt')
        regex_object = RegexPrinterMachine(regex='ain', full_files_path=[dummy_obj])
        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            regex_object.print()
        output = temp_stdout.getvalue().strip()
        with open('/project/tests/dummy_output1_machine.txt') as fp:
            output_result = fp.read()
        self.assertEqual(output, output_result)

if __name__ == '__main__':
    unittest.main()
