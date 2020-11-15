import unittest
import contextlib
from io import StringIO
from src.main import main
import sys


class TestRegex(unittest.TestCase):

    def test_invalid_regex_input(self):

        error_message_for_invalid_regex = sys.argv[0].split('\\')[-1]
        error_message_for_invalid_regex += ': error: argument -r/--regex: Error in function validate_regex: The regex expression is not valid'
        sys.argv.append('-f')
        sys.argv.append('/project/tests/dummy_input1.txt')
        sys.argv.append('-r')
        sys.argv.append('+')
        sys.argv.append('-m')
        temp_strout = StringIO()
        try:
            with contextlib.redirect_stderr(temp_strout):
                main()
        except:
            error_line = temp_strout.getvalue().strip().splitlines()[-1]
            # bring back the original sys.argv
            for par in sys.argv[1:]:
                sys.argv.remove(par)
            self.assertEqual(error_line, error_message_for_invalid_regex)

    def test_invalid_machine_input(self):

        error_message_for_invalid_machine_input = sys.argv[0].split('\\')[-1]
        error_message_for_invalid_machine_input += ": error: argument -m/--machine: Error in function handle_machine_input: The -m/--machine input expression is not valid" \
                                                   "\nOnly ['yes', 'true', 't', 'y', '1', True] are available"
        sys.argv.append('-f')
        sys.argv.append('/project/tests/dummy_input1.txt')
        sys.argv.append('-r')
        sys.argv.append('ain')
        sys.argv.append('-m')
        sys.argv.append('tyty')
        temp_strout = StringIO()
        try:
            with contextlib.redirect_stderr(temp_strout):
                main()
        except:
            error_line_2 = temp_strout.getvalue().strip().splitlines()[-2]
            error_line_1 = temp_strout.getvalue().strip().splitlines()[-1]
            full_error = error_line_2 + "\n" + error_line_1
            # bring back the original sys.argv
            for par in sys.argv[1:]:
                sys.argv.remove(par)
            self.assertEqual(full_error, error_message_for_invalid_machine_input)

    def test_invalid_color_input(self):

        error_message_for_invalid_color_input = sys.argv[0].split('\\')[-1]
        error_message_for_invalid_color_input += ": error: argument -c/--color: Error in function handle_color_input: The -c/--color input expression is not valid" \
                                                 "\nSupported format: blue/BLUE/Blue/blUe etc. Or the ANSI number."
        sys.argv.append('-f')
        sys.argv.append('/project/tests/dummy_input1.txt')
        sys.argv.append('-r')
        sys.argv.append('ain')
        sys.argv.append('-c')
        sys.argv.append('bluee')
        temp_strout = StringIO()
        try:
            with contextlib.redirect_stderr(temp_strout):
                main()
        except:
            error_line_2 = temp_strout.getvalue().strip().splitlines()[-2]
            error_line_1 = temp_strout.getvalue().strip().splitlines()[-1]
            full_error = error_line_2 + "\n" + error_line_1
            # bring back the original sys.argv
            for par in sys.argv[1:]:
                sys.argv.remove(par)
            self.assertEqual(full_error, error_message_for_invalid_color_input)

    def test_invalid_parameter(self):

        error_message_for_invalid_color_input = sys.argv[0].split('\\')[-1]
        error_message_for_invalid_color_input += ": error: argument -c/--color: Error in function handle_color_input: The -c/--color input expression is not valid" \
                                                 "\nSupported format: blue/BLUE/Blue/blUe etc. Or the ANSI number."
        sys.argv.append('-f')
        sys.argv.append('/project/tests/dummy_input1.txt')
        sys.argv.append('-r')
        sys.argv.append('ain')
        sys.argv.append('-ct')
        sys.argv.append('bluee')
        temp_strout = StringIO()
        try:
            with contextlib.redirect_stderr(temp_strout):
                main()
        except:
            error_line_2 = temp_strout.getvalue().strip().splitlines()[-2]
            error_line_1 = temp_strout.getvalue().strip().splitlines()[-1]
            full_error = error_line_2 + "\n" + error_line_1
            # bring back the original sys.argv
            for par in sys.argv[1:]:
                sys.argv.remove(par)
            self.assertEqual(full_error, error_message_for_invalid_color_input)

if __name__ == '__main__':
    unittest.main()
