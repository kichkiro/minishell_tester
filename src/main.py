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
    parsing = Tester(project_path, exe, "parsing", printer)
    commands = Tester(project_path, exe, "commands", printer)
    redirect = Tester(project_path, exe, "redirects", printer)
    exit_status = Tester(project_path, exe, "exit_status", printer)
    booleans = Tester(project_path, exe, "booleans", printer)
    wildcards = Tester(project_path, exe, "wildcards", printer)

    # PRE-TEST --------------------------------------------------------------->

    printer.section("PRE-TEST")
    utils.makefile("", True, project_path)
    utils.norminette(project_path)

    # PARSING ---------------------------------------------------------------->

    printer.section("Parsing")
    parsing.run()

    # COMMANDS --------------------------------------------------------------->

    printer.section("Commands")
    commands.run()

    # REDIRECTS -------------------------------------------------------------->

    printer.section("Redirects")
    redirect.run()

    # EXIT STATUS ------------------------------------------------------------>

    printer.section("Exit Status")
    exit_status.run()

    # BOOLEANS --------------------------------------------------------------->

    printer.section("Booleans")
    booleans.run()

    # WILDCARDS -------------------------------------------------------------->

    printer.section("Wildcards")
    wildcards.run()

    # SUMMARY ---------------------------------------------------------------->

    printer.summary()

if __name__ == "__main__":
    main()
