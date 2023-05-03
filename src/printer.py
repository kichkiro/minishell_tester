#!/usr/bin/python3

"""
Class that handles printing.
"""

# Libraries ------------------------------------------------------------------>

from termcolor import colored

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

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
        If all the tests pass, the function will exit. 
        If there are failed tests, it prompts the user to decide whether 
        to show the details of the failed tests or not.

    __banner()
        Print a formatted banner with ASCII art.

    __failed_test()
        Private method that handles the formatting and storage of failed 
        test logs.
        Thus, from each failed test, all information about the executed 
        test is taken and added to the self.failed_tests attribute.

    """
    def __init__(self) -> None:

        self.__banner()
        self.test_n = 1
        self.passed_tests_n = 0
        self.failed_tests_n = 0
        self.failed_tests = ""
        

    def section(self, msg:str) -> None:

        dashes = '-' * (68 - len(msg))
        print(colored(f"\n{msg} {dashes}>\n", "white", attrs=["bold"]))
        

    def result(
        self, status:str, loop:int, test:str, bash_output:str=None,
        minishell_output:str=None, bash_file_content:str=None,
        minishell_file_content:str=None, exception:str=None
    ) -> None:
        
        color = "green" if status == "OK" else "red"
        end = '\n' if (loop + 1) % 5 == 0 else ''
        extra_space = ' ' if (self.test_n) < 10 else ''
        print(colored(
            f"TEST {extra_space}{self.test_n}: {status} | ",
            color=color
        ), end=end)
        if status == "OK":
            self.passed_tests_n += 1
        elif status == "KO":
            self.failed_tests_n += 1
            self.__failed_test(test, bash_output, minishell_output, 
                bash_file_content, minishell_file_content, exception)
        self.test_n += 1


    def summary(self) -> None:
       
        self.section("SUMMARY")
        print(colored(
            f"PASSED: {self.passed_tests_n} test\s\n"
            f"FAILED: {self.failed_tests_n} test\s",
            color="blue"
        ))
        if not self.failed_tests_n:
            exit()
        quest = ""
        while quest != 'y' and quest != 'Y' and quest != 'n' and quest != 'N':
            quest = input(colored(
                "\nShow the failed tests? ([y]/n)? ", "blue"))
        if quest == 'y' or quest == 'Y':
            self.section("ERRORS")
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
    
    
    def __failed_test(
        self, test:str, bash_output:str, minishell_output:str,
        bash_file_content:str, minishell_file_content:str, exception:str
    ) -> None:
    
        test = test.replace('\n', '\\n')
        self.failed_tests += \
            f"\nTEST {self.test_n}: KO"\
            f"\n    Input:     [{test}]"
        if exception:
            self.failed_tests += \
                f"\n    Exception: {exception}"
        else:
            if bash_output != None and minishell_output != None:
                self.failed_tests += \
                    f"\n    Bash:      [{bash_output}]"\
                    f"\n    Minishell: [{minishell_output}]"
            if bash_file_content and minishell_file_content:
                self.failed_tests += \
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
                    self.failed_tests += f"\n        {key}: [{value}]"
                self.failed_tests += \
                    f"\n\n    Files content - Minishell:"
                for key, value in minishell_file_content.items():
                    value = value.strip('\n')
                    value = value.replace('\n', '\\n')
                    value = value.replace('\x1b', '')
                    self.failed_tests += f"\n        {key}: [{value}]"
        self.failed_tests += "\n\n" + ('-' * 70) + '\n'
