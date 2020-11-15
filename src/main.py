from src.utils import args_parser
from src.RegexPrinter import *


def main():
    args = args_parser()  # argparse.Namespace

    if args.color:
        search_printer = RegexPrinterByColor(regex=args.regex, full_files_path=args.files, color=args.color)
    elif args.machine:
        search_printer = RegexPrinterMachine(regex=args.regex, full_files_path=args.files)
    else:
        search_printer = RegexPrinter(regex=args.regex, full_files_path=args.files)

    search_printer.print()


if __name__ == "__main__":
    main()
