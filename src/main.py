#!/usr/bin/python3

"""
Tester for the Minishell project of school 42.
"""

# Libraries ------------------------------------------------------------------>

import os
import sys

from termcolor import colored
import utils
from tester import Tester
from printer import Printer

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# Functions ------------------------------------------------------------------>

def main():
    """
    """
    argv = sys.argv

    if len(argv) != 2:
        print(colored("\nWrong input arguments...\n", "red", attrs=["bold"]),
            file=sys.stderr)
        print(colored("[project_path]\n", "white"), file=sys.stderr)
        exit()

    project_path = os.path.abspath(argv[1])
    exe = "minishell"

    printer = Printer()
    echo = Tester(project_path, exe, "echo", printer)
    redirect = Tester(project_path, exe, "redirects", printer)
    heredoc = Tester(project_path, exe, "heredoc", printer)

    # PRE-TEST --------------------------------------------------------------->

    printer.section("PRE-TEST")
    utils.makefile("", True, project_path)

    # ECHO TEST -------------------------------------------------------------->

    printer.section("Echo - TEST")
    echo.run()

    # REDIRECTS TEST --------------------------------------------------------->

    printer.section("Redirects - TEST")
    redirect.run()

    # HEREDOC TEST ----------------------------------------------------------->

    # print()
    # printer.section("Heredoc - TEST")
    # heredoc.run()
    
    # SUMMARY ---------------------------------------------------------------->

    printer.summary()

if __name__ == "__main__":
    main()
