#!/usr/bin/python3

"""
Tester for the Minishell project of school 42.
"""

# Libraries ------------------------------------------------------------------>

import os
import sys
from typing import List

from termcolor import colored

import utils
from printer import Printer
from tester import Tester

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# Functions ------------------------------------------------------------------>


def main(argv: List[str]) -> None:
    """
    This is the main function of the program.

    Params
    --------------------------------------------------------------------
    argv : List[str]
        The list of arguments passed to the program.

    Returns
    --------------------------------------------------------------------
    None
    """
    project_path: str
    exe: str
    printer: Printer
    parsing: Tester
    commands: Tester
    redirect: Tester
    pipes: Tester
    exit_status: Tester
    mix_mandatory: Tester
    booleans: Tester
    wildcards: Tester
    # mix_bonus: Tester

    if len(argv) != 2:
        print(colored("\nWrong input arguments...\n", "red", attrs=["bold"]),
              file=sys.stderr)
        print(colored("[project_path]\n", "white"), file=sys.stderr)
        sys.exit()

    project_path: str = os.path.abspath(argv[1])
    exe: str = "minishell"

    printer = Printer()
    parsing = Tester(project_path, exe, "parsing", printer)
    commands = Tester(project_path, exe, "commands", printer)
    redirect = Tester(project_path, exe, "redirects", printer)
    pipes = Tester(project_path, exe, "pipes", printer)
    exit_status = Tester(project_path, exe, "exit_status", printer)
    mix_mandatory = Tester(project_path, exe, "mix_mandatory", printer)
    booleans = Tester(project_path, exe, "booleans", printer)
    wildcards = Tester(project_path, exe, "wildcards", printer)
    # mix_bonus = Tester(project_path, exe, "mix_bonus", printer)

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

    # PIPES ------------------------------------------------------------------>

    printer.section("Pipes")
    pipes.run()

    # EXIT STATUS ------------------------------------------------------------>

    printer.section("Exit Status")
    exit_status.run()

    # MIX MANDATORY ---------------------------------------------------------->

    printer.section("Mix Mandatory")
    mix_mandatory.run()

    # BOOLEANS --------------------------------------------------------------->

    printer.section("Booleans")
    booleans.run()

    # WILDCARDS -------------------------------------------------------------->

    printer.section("Wildcards")
    wildcards.run()

    # # MIX BONUS ------------------------------------------------------------>

    # printer.section("Mix Bonus")
    # mix_bonus.run()

    # SUMMARY ---------------------------------------------------------------->

    printer.summary()


if __name__ == "__main__":
    main(sys.argv)
