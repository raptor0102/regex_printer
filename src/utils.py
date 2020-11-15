import argparse
import inspect
import re


def validate_regex(regex: str) ->str:
    """
    Validate the regex expression.
    :param regex: the regex to check
    :return: str
    """
    try:
        re.compile(regex)
    except re.error:
        msg = "Error in function {}: The regex expression is not valid".format(inspect.currentframe().f_code.co_name)
        raise argparse.ArgumentTypeError(msg)
    return regex


def handle_machine_input(machine: str) ->bool:
    """
    Validate of the machine input
    :param machine: the machine input value
    :return: bool
    """
    if isinstance(machine, bool):
        return True
    elif machine.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    else:
        msg = "Error in function {}: The -m/--machine input expression is not valid" \
              "\nOnly ['yes', 'true', 't', 'y', '1', True] are available".format(inspect.currentframe().f_code.co_name)
        raise argparse.ArgumentTypeError(msg)


def handle_color_input(color: str) ->str:
    """
    Convert the color input into AnsiColorEnum Enum object. Can be either: BLUE/blue/34
    :return: str
    """
    ansi_color_enum_dict = {"BLACK": 30,
                            "RED": 31,
                            "GREEN": 32,
                            "YELLOW": 33,
                            "BLUE": 34,
                            "MAGENTA": 35,
                            "CYAN": 36,
                            "WHITE": 37}
    try:
        if str(color).isdigit() and int(color) in ansi_color_enum_dict.values():
            return str(color)
        else:
            return ansi_color_enum_dict[str(color).upper()]
    except KeyError:
        msg = "Error in function {}: The -c/--color input expression is not valid" \
              "\nSupported format: blue/BLUE/Blue/blUe etc. Or the ANSI number."\
            .format(inspect.currentframe().f_code.co_name)
        raise argparse.ArgumentTypeError(msg)


def args_parser() -> argparse.Namespace:
    """
    Create an argparse object and initialize all the script inputs
    :return: argparse.Namespace object
    """
    # Construct the argument parser
    ap = argparse.ArgumentParser(description='Python module that receives a regex expression and file(s) as an input, '
                                             'and searches for regex matches inside those files',
                                 add_help=False,
                                 usage="\nrequired inputs:"
                                       "\n\t 1. -f/--file (lower case) input single or many files"
                                       "\n\t 2. -r/--regex (lower case) regex expression the module will use"
                                       "\noptional inputs (mutually_exclusive - only one of them can be used):"
                                       "\n\t 1. [-c/--color] (lower case) highlight matching text"
                                       "\n\t 2. [-m/--machine] (lower case) machine-readable output")
    # Add input arguments and using 'nargs' parameter in order to receive as an input at least single file
    ap.add_argument("-f", "--files", type=argparse.FileType('r'), nargs='+', required=True,
                    help="Full files path to search using the regex expression", )
    ap.add_argument("-r", "--regex", type=validate_regex, required=True,
                    help="regex expression to search in file(s)")  # search_regex_script
    # Add mutually exclusive inputs
    group = ap.add_mutually_exclusive_group(required=False)
    group.add_argument("-c", "--color", type=handle_color_input, help="highlight matching text")
    group.add_argument("-m", "--machine", help="generate machine-readable output", type=handle_machine_input,
                       nargs='?', const=True, default=False)  # Store True in case of no argument follow the -m input

    # Process the arguments and check for valid regex expression
    args = ap.parse_args()

    return args
