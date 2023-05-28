#!/usr/bin/python3

"""
Class that handles printing.
"""

# Libraries ------------------------------------------------------------------>

import sys
from typing import Union, Dict

from termcolor import colored

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# Functions ------------------------------------------------------------------>


class Printer:
    """
    Attributes
    --------------------------------------------------------------------
    test_n : int
        Counter keeping track of the number of tests.

    passed_tests_n : int
        Counter keeping track of the number of tests passed.

    failed_tests_n : int
        Counter tracking the number of failed tests.

    failed_tests : str
        String containing logs of failed tests.

    passed_tests : str
        String containing logs of passed tests.

    Methods
    --------------------------------------------------------------------
    section(msg):
        Print a section header with a message and dashes to visually
        separate the sections.

    result(status, loop, test, bash_output, minishell_output,
        exit_status, exit_status_path):
        Print the results of a test in a formatted way, indicating
        whether the test passed or failed.

    summary():
        The summary function prints the total number of passed and
        failed tests.
        It also asks the user whether he/she wants to see passed and/or
        failed tests or exit.

    __archive(status, loop, test, bash_output, minishell_output,
        exit_status, exit_status_path):
        Private method that handles the formatting and storage of passed
        or failed test.
        Thus, from each passed or failed test, all information about the
        executed test is taken and added to the self.passed_tests or
        self.failed_tests attribute.
    """

    print(colored(
        "\n"
        "░░░╗   ░░░╗░░╗░░░╗   ░░╗░░╗░░░░░░░╗░░╗  ░░╗░░░░░░░╗░░╗     ░░╗     \n"
        "░░░░╗ ░░░░║░░║░░░░╗  ░░║░░║░░╔════╝░░║  ░░║░░╔════╝░░║     ░░║     \n"
        "░░╔░░░░╔░░║░░║░░╔░░╗ ░░║░░║░░░░░░░╗░░░░░░░║░░░░░╗  ░░║     ░░║     \n"
        "░░║╚░░╔╝░░║░░║░░║╚░░╗░░║░░║╚════░░║░░╔══░░║░░╔══╝  ░░║     ░░║     \n"
        "░░║ ╚═╝ ░░║░░║░░║ ╚░░░░║░░║░░░░░░░║░░║  ░░║░░░░░░░╗░░░░░░░╗░░░░░░░╗\n"
        "╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝\n"
        "                                                                   \n"
        "░░░░░░░░╗░░░░░░░╗░░░░░░░╗░░░░░░░░╗░░░░░░░╗░░░░░░╗                  \n"
        "╚══░░╔══╝░░╔════╝░░╔════╝╚══░░╔══╝░░╔════╝░░╔══░░╗                 \n"
        "   ░░║   ░░░░░╗  ░░░░░░░╗   ░░║   ░░░░░╗  ░░░░░░╔╝                 \n"
        "   ░░║   ░░╔══╝  ╚════░░║   ░░║   ░░╔══╝  ░░╔══░░╗                 \n"
        "   ░░║   ░░░░░░░╗░░░░░░░║   ░░║   ░░░░░░░╗░░║  ░░║                 \n"
        "   ╚═╝   ╚══════╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝                  ",
        "blue"
    ))

    def __init__(self) -> None:

        self.test_n: int
        self.passed_tests_n: int
        self.failed_tests_n: int
        self.passed_tests: str
        self.failed_tests: str

        self.test_n = 1
        self.passed_tests_n = 0
        self.failed_tests_n = 0
        self.passed_tests = ""
        self.failed_tests = ""

    def section(self, msg: str) -> None:
        """
        Print a section header with a message and dashes to visually
        separate the sections.

        Params
        ----------------------------------------------------------------
        msg : str
            Message to be printed.

        Returns
        ----------------------------------------------------------------
        None
        """
        dashes: str

        dashes = '-' * (73 - len(msg))
        print(colored(f"\n{msg} {dashes}>\n", "white", attrs=["bold"]))

    def result(self, status: str, loop: int, test: str, excep: str = None,
               output_data: Dict[str, Union[str, int]] = None) -> None:
        """
        Print the results of a test in a formatted way, indicating
        whether the test passed or failed.

        Params
        ----------------------------------------------------------------
        status : str
            Status of the test, either "OK" or "KO".
        loop : int
            Number of the loop in which the test was executed.
        test : str
            Name of the test.
        excep : str
            Exception raised by the test, if any.
        output_data : Dict[str, Union[str, int]]
            Dictionary containing the output data of the test.

        Returns
        ----------------------------------------------------------------
        None
        """
        color: str
        end: str
        extra_space: str

        color = "green" if status == "OK" else "red"
        end = '\n' if (loop + 1) % 5 == 0 else ''
        extra_space = ''
        if self.test_n < 10:
            extra_space = '  '
        elif self.test_n < 100:
            extra_space = ' '
        print(colored(
            f"TEST {extra_space}{self.test_n}: {status} | ",
            color=color
        ), end=end, flush=True)
        if status == "OK":
            self.passed_tests_n += 1
        elif status == "KO":
            self.failed_tests_n += 1
        self.__archive(test, status, excep=excep, out=output_data)
        self.test_n += 1

    def summary(self) -> None:
        """
        Print a summary of the tests executed, indicating the number of
        tests passed and failed. If there are failed tests, the user is
        asked whether they want to see the details of the failed tests.

        Params
        ----------------------------------------------------------------
        None

        Returns
        ----------------------------------------------------------------
        None
        """
        quest: str

        self.section("SUMMARY")
        print(colored(
            f"PASSED: {self.passed_tests_n} tests\n"
            f"FAILED: {self.failed_tests_n} tests",
            color="blue"
        ))
        if self.failed_tests_n > 0 and self.passed_tests_n > 0:
            quest = ""
            while quest not in ['1', '2', 'n', 'N']:
                quest = input(colored(
                    "\nPress [1] to see passed tests, [2] for failed, [n] to "
                    "exit ([1/2]/n)? ", "blue"))
            if quest == '1':
                self.section("PASSED")
                print(colored(self.passed_tests, "green"))
                quest = ""
                while quest not in ['2', 'n', 'N']:
                    quest = input(colored(
                        "\nPress [2] to see failed tests, [n] to exit "
                        "([2]/n)? ", "blue"))
                if quest == '2':
                    self.section("FAILED")
                    print(colored(self.failed_tests, "red"))
                else:
                    sys.exit()
            elif quest == '2':
                self.section("FAILED")
                print(colored(self.failed_tests, "red"))
                while quest not in ['1', 'n', 'N']:
                    quest = input(colored(
                        "\nPress [1] to see passed tests, [n] to exit "
                        "([1]/n)? ", "blue"))
                if quest == '1':
                    self.section("PASSED")
                    print(colored(self.passed_tests, "green"))
            else:
                sys.exit()
        elif self.passed_tests_n > 0 and self.failed_tests_n == 0:
            quest = ""
            while quest not in ['1', 'n', 'N']:
                quest = input(colored(
                    "\nPress [1] to see passed tests, [n] to exit "
                    "([1]/n)? ", "blue"))
            if quest == '1':
                self.section("PASSED")
                print(colored(self.passed_tests, "green"))
            else:
                sys.exit()
        elif self.passed_tests_n == 0 and self.failed_tests_n > 0:
            quest = ""
            while quest not in ['2', 'n', 'N']:
                quest = input(colored(
                    "\nPress [2] to see failed tests, [n] to exit "
                    "([2]/n)? ", "blue"))
            if quest == '2':
                self.section("FAILED")
                print(colored(self.failed_tests, "red"))
            else:
                sys.exit()

    def __archive(self, test: str, status: str, excep: Union[str, None],
                  out: Dict[str, Union[str, None]] = None) -> None:
        """
        Archive the results of a test in a formatted way, indicating
        whether the test passed or failed.

        Params
        ----------------------------------------------------------------
        test : str
            Name of the test.
        status : str
            Status of the test, either "OK" or "KO".
        excep : str
            Exception raised by the test, if any.
        out : Dict[str, Union[str, None]]
            Dictionary containing the output data of the test.

        Returns
        ----------------------------------------------------------------
        None
        """
        archive: str
        error: str

        if status == "OK":
            archive = self.passed_tests
        else:
            archive = self.failed_tests

        test = test.replace('\n', '\\n')
        archive += \
            f"\nTEST {self.test_n}: {status}"\
            f"\n    Input:        [{test}]"
        if excep is not None:
            error = str(excep)
            if len(error) > 52:
                error = error[:52] + '\n' + (' ' * 17) + error[52:]
            archive += \
                f"\n    Exception:    {error}"
        elif out is not None:
            if out["bash_out"] is not None\
                    and out["minishell_out"] is not None:
                bash_output = out["bash_out"].replace('\n', '\\n')
                minishell_output = out["minishell_out"].replace('\n', '\\n')
                archive += \
                    f"\n    Bash:         [{bash_output}]"\
                    f"\n    Minishell:    [{minishell_output}]"
            if out["bash_exit_status"] is not None\
                    and out["minishell_exit_status"] is not None:
                archive += \
                    f"\n    Bash $?:      [{out['bash_exit_status']}]"\
                    f"\n    Minishell $?: [{out['minishell_exit_status']}]"
            if out["bash_file_content"] and out["minishell_file_content"]:
                archive += \
                    "\n\n    Lab creation:"\
                    "\n        cat 1 > file1"\
                    "\n        cat 2 > file2"\
                    "\n        cat 3 > file3"\
                    "\n        cat 4 > file4"\
                    "\n\n    Files content - Bash:"
                for key, value in out["bash_file_content"].items():
                    value = value.strip('\n')
                    value = value.replace('\n', '\\n')
                    value = value.replace('\x1b', '')
                    archive += f"\n        {key}: [{value}]"
                archive += \
                    "\n\n    Files content - Minishell:"
                for key, value in out["minishell_file_content"].items():
                    value = value.strip('\n')
                    value = value.replace('\n', '\\n')
                    value = value.replace('\x1b', '')
                    archive += f"\n        {key}: [{value}]"
        archive += "\n\n" + ('-' * 70) + '\n'

        if status == "OK":
            self.passed_tests = archive
        else:
            self.failed_tests = archive
