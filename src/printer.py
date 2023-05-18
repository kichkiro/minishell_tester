#!/usr/bin/python3

"""
Class that handles printing.
"""

# Libraries ------------------------------------------------------------------>

from typing import Union
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
    section():
        Print a section header with a message and dashes to visually 
        separate the sections.

    result():
        Print the results of a test in a formatted way, indicating 
        whether the test passed or failed.

    summary():
        The summary function prints the total number of passed and 
        failed tests.
        It also asks the user whether he/she wants to see passed and/or 
        failed tests or exit.

    __banner()
        Print a formatted banner with ASCII art.

    __archive()
        Private method that handles the formatting and storage of passed
        or failed test.
        Thus, from each passed or failed test, all information about the 
        executed test is taken and added to the self.passed_tests or
        self.failed_tests attribute.

    """
    def __init__(self) -> None:

        self.test_n:int
        self.passed_tests_n:int
        self.failed_tests_n:int
        self.passed_tests:str
        self.failed_tests:str

        self.__banner()
        self.test_n = 1
        self.passed_tests_n = 0
        self.failed_tests_n = 0
        self.passed_tests = ""
        self.failed_tests = ""
        

    def section(self, msg:str) -> None:

        dashes:str

        dashes = '-' * (73 - len(msg))
        print(colored(f"\n{msg} {dashes}>\n", "white", attrs=["bold"]))
        

    def result(
        self, status:str, loop:int, test:str, 
        bash_output:Union[str,None]=None,
        minishell_output:Union[str,None]=None, 
        bash_file_content:Union[dict,None]=None,
        minishell_file_content:Union[dict,None]=None, 
        exception:Union[str,None]=None, 
        bash_exit_status:Union[int,None]=None, 
        minishell_exit_status:Union[int,None]=None
    ) -> None:
        
        color:str
        end:str
        extra_space:str

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
        self.__archive(test, status, bash_output, minishell_output, 
            bash_file_content, minishell_file_content, exception,
            bash_exit_status, minishell_exit_status)
        self.test_n += 1


    def summary(self) -> None:

        quest:str
       
        self.section("SUMMARY")
        print(colored(
            f"PASSED: {self.passed_tests_n} tests\n"
            f"FAILED: {self.failed_tests_n} tests",
            color="blue"
        ))
        if self.failed_tests_n > 0 and self.passed_tests_n > 0:
            quest = ""
            while quest != '1' and quest != '2' and quest != 'n' and \
                quest != 'N':
                quest = input(colored(
                    "\nPress [1] to see passed tests, [2] for failed, [n] to "
                    "exit ([1/2]/n)? ", "blue"))
            if quest == '1':
                self.section("PASSED")
                print(colored(self.passed_tests, "green"))
                quest = ""
                while quest != '2' and quest != 'n' and quest != 'N':
                    quest = input(colored(
                        "\nPress [2] to see failed tests, [n] to exit "
                        "([2]/n)? ", "blue"))
                if quest == '2':
                    self.section("FAILED")
                    print(colored(self.failed_tests, "red"))
                else:
                    exit()
            elif quest == '2':
                self.section("FAILED")
                print(colored(self.failed_tests, "red"))
                while quest != '1' and quest != 'n' and quest != 'N':
                    quest = input(colored(
                        "\nPress [1] to see passed tests, [n] to exit "
                        "([1]/n)? ", "blue"))
                if quest == '1':
                    self.section("PASSED")
                    print(colored(self.passed_tests, "green"))
            else:
                exit()
        elif self.passed_tests_n > 0 and self.failed_tests_n == 0:
            quest = ""
            while quest != '1' and quest != 'n' and quest != 'N':
                quest = input(colored(
                    "\nPress [1] to see passed tests, [n] to exit "
                    "([1]/n)? ", "blue"))
            if quest == '1':
                self.section("PASSED")
                print(colored(self.passed_tests, "green"))
            else:
                exit()
        elif self.passed_tests_n == 0 and self.failed_tests_n > 0:
            quest = ""
            while quest != '2' and quest != 'n' and quest != 'N':
                quest = input(colored(
                    "\nPress [2] to see failed tests, [n] to exit "
                    "([2]/n)? ", "blue"))
            if quest == '2':
                self.section("FAILED")
                print(colored(self.failed_tests, "red"))
            else:
                exit()


    def __banner(self) -> None:

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
    
    
    def __archive(
        self, test:str, status:str, bash_output:Union[str,None], 
        minishell_output:Union[str,None], bash_file_content:Union[dict,None], 
        minishell_file_content:Union[dict,None], exception:Union[str,None], 
        bash_exit_status:Union[int,None]=None, 
        minishell_exit_status:Union[int,None]=None
    ) -> None:
        
        archive:str
        error:str
        
        if status == "OK":
            archive = self.passed_tests
        else:
            archive = self.failed_tests
    
        test = test.replace('\n', '\\n')
        archive += \
            f"\nTEST {self.test_n}: {status}"\
            f"\n    Input:        [{test}]"
        if exception:
            error = str(exception)
            if len(error) > 52:
                error = error[:52] + '\n' + (' ' * 17) + error[52:]
            archive += \
                f"\n    Exception:    {error}"
        else:
            if bash_output != None and minishell_output != None:
                bash_output = bash_output.replace('\n', '\\n')
                minishell_output = minishell_output.replace('\n', '\\n')
                archive += \
                    f"\n    Bash:         [{bash_output}]"\
                    f"\n    Minishell:    [{minishell_output}]"
            if bash_exit_status != None and minishell_exit_status != None:
                archive += \
                    f"\n    Bash $?:      [{bash_exit_status}]"\
                    f"\n    Minishell $?: [{minishell_exit_status}]"
            if bash_file_content and minishell_file_content:
                archive += \
                    f"\n\n    Lab creation:"\
                    f"\n        cat 1 > file1"\
                    f"\n        cat 2 > file2"\
                    f"\n        cat 3 > file3"\
                    f"\n        cat 4 > file4"\
                    f"\n\n    Files content - Bash:"
                for key, value in bash_file_content.items():
                    value = value.strip('\n')
                    value = value.replace('\n', '\\n')
                    value = value.replace('\x1b', '')
                    archive += f"\n        {key}: [{value}]"
                archive += \
                    f"\n\n    Files content - Minishell:"
                for key, value in minishell_file_content.items():
                    value = value.strip('\n')
                    value = value.replace('\n', '\\n')
                    value = value.replace('\x1b', '')
                    archive += f"\n        {key}: [{value}]"
        archive += "\n\n" + ('-' * 70) + '\n'
        if status == "OK":
            self.passed_tests = archive
        else:
            self.failed_tests = archive
