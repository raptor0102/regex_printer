from collections import OrderedDict
import threading
import re
import os
from colorama import Fore


class RegexPrinter(object):
    def __init__(self, regex: str, full_files_path: list):
        self.regex = regex  # Which Regex to use to search in the files
        # initialize the files path according to the argparse input, for single or many files
        self.list_of_files = [file.name for file in full_files_path]
        self.dictionary_file_and_info = {file: OrderedDict() for file in self.list_of_files}
        # In case of many files without
        # Read all the files and search a regex match text for each line
        list_threads = []
        for i, file in enumerate(self.list_of_files):
            t = threading.Thread(name='file_num_{}'.format(i), target=self.search_regex, args=(file,))
            t.start()
            list_threads.append(t)
        [t.join() for t in list_threads]
        # Code for non parallel
        # for file in self.list_of_files:
        #     self.search_regex(file_path=file)

    def search_regex(self, file_path: str) -> None:
        """
        Read single file and search a regex match text for each line, store the full line, line number and
        the start and the end index position for each match.
        :param file_path: Full file path for single input file
        :return: None
        """
        # Starting to search according to the regex, line by line in specific single file
        with open(file_path) as fp:
            for cnt, line in enumerate(fp, 1):
                for match in re.finditer(self.regex, line):
                    temp_tuple = (match.start(), match.end())
                    fixed_line = line.rstrip('\n')
                    key_for_file = str(cnt) + "-" + str(fixed_line)
                    if key_for_file not in self.dictionary_file_and_info[file_path]:
                        self.dictionary_file_and_info[file_path][key_for_file] = []
                    self.dictionary_file_and_info[file_path][key_for_file].append(temp_tuple)

    def print(self) -> None:
        """
        Print to the standard output the matching of the regex for each file.
        Each match will be in a different line such as:
         <FileName>:<FullLine>:<LineNumber>:<MatchingText>
         Example for file: file1.txt:

        'ainfmain iu
        gty
            756
        ainainain
        dfsdf'

        and regex is 'ain'
         Output will be:

        input.txt:ainfmain iu:1:ain
        input.txt:ainfmain iu:1:ain
        input.txt:ainainain:5:ain
        input.txt:ainainain:5:ain
        input.txt:ainainain:5:ain
        :return: None
        """

        for file in self.list_of_files:
            base_name = os.path.basename(file)
            for full_line, line_indexing in self.dictionary_file_and_info[file].items():
                split_key = full_line.split('-')  # Split the key by delimiter: '-' First value represents the
                # line_number. All the next elements represents the full line
                line = '-'.join(split_key[1:])
                line_number = split_key[0]
                template_result_to_print = "{file_name}:{full_line}:{line_number}:".format(file_name=base_name,
                                                                                           full_line=line,
                                                                                           line_number=line_number)
                for single_index in line_indexing:
                    result_to_print = template_result_to_print
                    start_index = single_index[0]
                    end_index = single_index[1]
                    result_to_print += line[start_index:end_index]
                    print(result_to_print)


class RegexPrinterByColor(RegexPrinter):

    def __init__(self, **kwargs):
        self.color = kwargs.pop('color', None)
        super().__init__(**kwargs)

    def print(self, file_path: str = "") -> None:
        """
        Print to the standard output the matching of the regex for each file with the specified color.
        The matching values will be colored inline in the full line output
         <FileName>:<FullLine>:<LineNumber>:<MatchingText>
         Example for file: file1.txt:

        'ainfmain iu
        gty
            756
        ainainain
        dfsdf'

        and regex is 'ain'
         Output will be:

        input.txt:<ain>fm<ain> iu:1
        input.txt:<ainainain>:5
        :return: None
        """
        for file in self.list_of_files:
            base_name = os.path.basename(file)
            for full_line, line_indexing in self.dictionary_file_and_info[file].items():
                split_key = full_line.split('-')  # Split the key by delimiter: '-' First value represents the
                # line_number. All the next elements represents the full line
                line = '-'.join(split_key[1:])
                line_number = split_key[0]
                colored_result = ""
                for i, single_index in enumerate(line_indexing, 1):
                    start_index = single_index[0]
                    end_index = single_index[1]
                    if i == 1:
                        colored_result += line[:start_index]
                    else:
                        previous_index = line_indexing[i - 2][1]
                        colored_result += line[previous_index:start_index]
                    colored_result += '[{}m'.format(self.color)
                    colored_result += line[start_index:end_index]
                    colored_result += Fore.RESET
                    if i == len(line_indexing):
                        colored_result += line[end_index:]

                template_result_to_print = "{file_name}:{full_line}:{line_number}".format(file_name=base_name,
                                                                                          full_line=colored_result,
                                                                                          line_number=line_number)
                print(template_result_to_print)


class RegexPrinterMachine(RegexPrinter):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def print(self) -> None:
        """
        Print to the standard output the matching of the regex for each file.
        Each match will be in a different line such as:
         <FileName>:<LineNumber>:<StartPosition>:<MatchingText>
         format: file_name:no_line:start_pos:matched_text
         Example for file: file1.txt:

        'ainfmain iu
        gty
            756
        ainainain
        dfsdf'

        and regex is 'ain'
         Output will be:

        input.txt:1:0:ain
        input.txt:1:5:ain
        input.txt:5:0:ain
        input.txt:5:3:ain
        input.txt:5:6:ain
        :return: None
        """

        for file in self.list_of_files:
            base_name = os.path.basename(file)
            for full_line, line_indexing in self.dictionary_file_and_info[file].items():
                split_key = full_line.split('-')  # Split the key by delimiter: '-' First value represents the
                # line_number. All the next elements represents the full line
                line = '-'.join(split_key[1:])
                line_number = split_key[0]
                template_result_to_print = "{file_name}:{line_number}:".format(file_name=base_name,
                                                                               line_number=line_number)
                for single_index in line_indexing:
                    result_to_print = template_result_to_print
                    start_index = single_index[0]
                    end_index = single_index[1]
                    result_to_print += "{start_pos}:".format(start_pos=start_index)
                    result_to_print += line[start_index:end_index]
                    print(result_to_print)
