#!/usr/bin/python3

"""
A set of utils functions.
"""

# Libraries ------------------------------------------------------------------>

import sys
import subprocess

from termcolor import colored

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# Functions ------------------------------------------------------------------>


def makefile(rules: str, must_print: bool, project_path: str):
    """
    Run the make command with specified rules on a given project path.

    Params
    --------------------------------------------------------------------
    rules : str
        The makefile rules to run.
    must_print : bool
        Whether to print output or not.
    project_path : str
        The path to the project directory.

    Returns
    --------------------------------------------------------------------
    None
    """
    process: subprocess.Popen

    if rules != "":
        process = subprocess.Popen(
            ["make", rules, "-C", project_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    else:
        process = subprocess.Popen(
            ["make", "-C", project_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
    _, stderr = process.communicate()
    if not process.returncode and must_print:
        print(colored("Make: OK\n", "green",))
    elif process.returncode:
        print(colored(f"Make: KO!\n\n    {stderr.decode('utf-8')}", "red"))
        sys.exit(1)


def norminette(project_path: str):
    """
    Run the norminette command on a given project path.

    Params
    --------------------------------------------------------------------
    project_path:str
        The path to the project directory.
    Returns
    --------------------------------------------------------------------
    None
    """
    process: subprocess.Popen

    process = subprocess.Popen(
        ["norminette", project_path],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    process.communicate()
    if not process.returncode:
        print(colored("Norminette: OK", "green"))
    else:
        print(colored("Norminette: Error!", "red"))
