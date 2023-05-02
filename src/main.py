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
        print(colored("\nWrong input arguments...\n", "red", attrs=["bold"]))
        print(colored("[project_path]\n", "white"))
        exit()

    project_path = os.path.abspath(argv[1])
    exe = "minishell"

    utils.banner()

    echo = Tester(project_path, exe, "echo")
    redirect = Tester(project_path, exe, "redirects")

    # PRE-TEST --------------------------------------------------------------->

    print(colored(
        "PRE-TEST ---------------------------------------------------------->"
        "\n", 
        "white", 
        attrs=["bold"]
    ))

    utils.makefile("", True, project_path)

    # ECHO TEST -------------------------------------------------------------->

    print(colored(
        "Echo - TEST ------------------------------------------------------->"
        "\n",
        "white", 
        attrs=["bold"]
    ))

    echo.run()

    # REDIRECTS TEST --------------------------------------------------------->

    print(colored(
        "Redirects - TEST -------------------------------------------------->"
        "\n",
        "white", 
        attrs=["bold"]
    ))

    redirect.run()

if __name__ == "__main__":
    main()
