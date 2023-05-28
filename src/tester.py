#!/usr/bin/python3

"""
A class to run a set of tests on a given project and evaluate the
results.
"""

# Libraries ------------------------------------------------------------------>

import os
from typing import List, Dict, Union

from termcolor import colored

import tests
from lab import Lab
from printer import Printer
from process import Process

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# Functions ------------------------------------------------------------------>


class Tester:
    """
    Attributes
    --------------------------------------------------------------------
    name : str
        The name of the test.

    project_path : str
        The path to the project directory.

    cmd : List[str]
        The command to run the executable.

    printer : Printer
        The printer object.

    tests : List[str]
        The list of tests to run.

    Methods
    --------------------------------------------------------------------
    run():
        Runs the test cases and prints the results.

    __exec(process, test, loop):
        Executes a test case using the provided process object, test
        name, and loop index.
        Compares the output of the test case in both Bash and Minishell
        and prints the result.

    __exec2(process, test, loop, lab):
        Executes a test case using the provided process object,
        test name, loop index, and lab object.
        Compares the output and file contents of the test case in both
        Bash and Minishell and prints the result.

    __exitstatus(process, test, loop, lab):
        Executes a test case to check the exit status using the provided
        process object, test name, loop index, and lab object.
        Compares the exit status of the test case in both Bash and
        Minishell and prints the result.

    __wildcards(process, test, loop, lab):
        Executes a test case with wildcard expansion using the provided
        process object, test name, loop index, and lab object.
        Compares the output of the test case in both Bash and Minishell
        and prints the result.

    Notes
    --------------------------------------------------------------------
    The Tester class is designed to run tests on a project executable.
    The test cases are run using subprocess.Popen, which allows for
    running external programs and capturing their output.
    """
    def __init__(self, path: str, exe: str, test: str, printer: Printer)\
            -> None:

        self.name: str
        self.project_path: str
        self.cmd: str
        self.printer: Printer
        self.tests: List[str]

        self.name = test
        self.project_path = path
        self.cmd = f"{path}/{exe}"
        self.printer = printer
        if test == "parsing":
            self.tests = tests.parsing
        elif test == "commands":
            self.tests = tests.commands
        elif test == "redirects":
            self.tests = tests.redirects
        elif test == "pipes":
            self.tests = tests.pipes
        elif test == "exit_status":
            self.tests = tests.exit_status
        elif test == "mix_mandatory":
            self.tests = tests.mix_mandatory
        elif test == "booleans":
            self.tests = tests.booleans
        elif test == "wildcards":
            self.tests = tests.wildcards
        # elif test == "mix_bonus":
        #     self.tests = tests.mix_bonus

    def run(self) -> None:
        """
        Runs the test cases and prints the results.

        Params
        ----------------------------------------------------------------
        None

        Returns
        ----------------------------------------------------------------
        None
        """
        loop: int
        test: str
        lab: Lab
        process: Process

        loop = 0
        for test in self.tests:
            lab = Lab(self.name)
            os.chdir(lab.path)
            process = Process(self.cmd, self.printer)
            try:
                if self.name == "parsing":
                    self.__exec(process, test, loop)
                elif self.name == "commands":
                    self.__exec(process, test, loop)
                elif self.name == "redirects":
                    self.__exec2(process, test, loop, lab)
                elif self.name == "pipes":
                    self.__exec2(process, test, loop, lab)
                elif self.name == "exit_status":
                    self.__exitstatus(process, test, loop, lab)
                elif self.name == "mix_mandatory":
                    self.__exec2(process, test, loop, lab)
                elif self.name == "booleans":
                    self.__exec(process, test, loop)
                elif self.name == "wildcards":
                    self.__wildcards(process, test, loop, lab)
                # elif self.name == "mix_bonus":
                #     self.__exec2(process, test, loop, lab)
            except Exception as err:
                print(colored(f"abc -Exception: {err}", "red"))
            finally:
                lab.remove()
                loop += 1

    def __exec(self, process: Process, test: str, loop: int) -> None:
        """
        Executes a test case using the provided process object, test
        name, and loop index.
        Compares the output of the test case in both Bash and Minishell
        and prints the result.

        Params
        ----------------------------------------------------------------
        process : Process
            The process object.
        test : str
            The name of the test case.
        loop : int
            The index of the test case.

        Returns
        ----------------------------------------------------------------
        None
        """
        bash_out: str
        minishell_out: Union[str, None]
        output_data: Dict[str, str]

        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, False)
        if minishell_out is None:
            return

        bash_out = bash_out.strip('\n')
        minishell_out = minishell_out.strip('\n')
        output_data = {
            "bash_out": bash_out,
            "minishell_out": minishell_out,
            "bash_file_content": None,
            "minishell_file_content": None,
            "bash_exit_status": None,
            "minishell_exit_status": None,
        }

        if bash_out in (minishell_out, minishell_out[:-1]):
            self.printer.result("OK", loop, test, output_data=output_data)
        else:
            self.printer.result("KO", loop, test, output_data=output_data)

    def __exec2(self, process: Process, test: str, loop: int, lab: Lab)\
            -> None:
        """
        Executes a test case using the provided process object,
        test name, loop index, and lab object.
        Compares the output and file contents of the test case in both
        Bash and Minishell and prints the result.

        Params
        ----------------------------------------------------------------
        process : Process
            The process object.
        test : str
            The name of the test case.
        loop : int
            The index of the test case.
        lab : Lab
            The lab object.

        Returns
        ----------------------------------------------------------------
        None
        """
        test_files: List[str]
        bash_out: str
        minishell_out: str
        bash_file_content: Dict[str, str]
        minishell_file_content: Dict[str, str]
        output_data: Dict[str, str]

        test_files = lab.create_redirects_lab()
        bash_out = process.get_bash_output(test)
        bash_file_content = {}
        for test_file in test_files:
            with open(test_file, "r", encoding="utf-8") as file:
                bash_file_content[test_file[-5:]] = file.read()
        lab.remove_redirects_lab(test_files)

        test_files = lab.create_redirects_lab()
        minishell_out = process.get_minishell_output_pty(bash_out, test)
        if minishell_out is None:
            return
        minishell_file_content = {}
        for test_file in test_files:
            with open(test_file, "r", encoding="utf-8") as file:
                minishell_file_content[test_file[-5:]] = file.read()
        lab.remove_redirects_lab(test_files)

        bash_out = bash_out.strip('\n')
        minishell_out = minishell_out.strip('\n')
        output_data = {
            "bash_out": bash_out,
            "minishell_out": minishell_out,
            "bash_file_content": bash_file_content,
            "minishell_file_content": minishell_file_content,
            "bash_exit_status": None,
            "minishell_exit_status": None,
        }

        if bash_out in (minishell_out, minishell_out[:-1]) and \
                minishell_file_content == bash_file_content:
            self.printer.result("OK", loop, test, output_data=output_data)
        else:
            self.printer.result("KO", loop, test, output_data=output_data)

    def __exitstatus(self, process: Process, test: str, loop: int, lab: Lab)\
            -> None:
        """
        Executes a test case using the provided process object,
        test name, loop index, and lab object.
        Compares the exit status of the test case in both Bash and
        Minishell and prints the result.

        Params
        ----------------------------------------------------------------
        process : Process
            The process object.
        test : str
            The name of the test case.
        loop : int
            The index of the test case.
        lab : Lab
            The lab object.

        Returns
        ----------------------------------------------------------------
        None
        """
        test_file: str
        bash_out: str
        minishell_out: Union[str, None]
        output_data: Dict[str, str]

        test_file = lab.create_exit_status_lab()
        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, True)
        lab.remove_exit_status_lab(test_file)
        if minishell_out is None:
            return

        output_data = {
            "bash_out": None,
            "minishell_out": None,
            "bash_file_content": None,
            "minishell_file_content": None,
            "bash_exit_status": process.exit_status_bash,
            "minishell_exit_status": process.exit_status_minishell,
        }

        if process.exit_status_bash == process.exit_status_minishell:
            self.printer.result("OK", loop, test, output_data=output_data)
        else:
            self.printer.result("KO", loop, test, output_data=output_data)

    def __wildcards(self, process: Process, test: str, loop: int, lab: Lab)\
            -> None:
        """
        Executes a test case using the provided process object,
        test name, loop index, and lab object.
        Compares the output of the test case in both Bash and Minishell
        and prints the result.

        Params
        ----------------------------------------------------------------
        process : Process
            The process object.
        test : str
            The name of the test case.
        loop : int
            The index of the test case.
        lab : Lab
            The lab object.

        Returns
        ----------------------------------------------------------------
        None
        """
        files: List[str]
        dirs: List[str]
        bash_out: str
        minishell_out: Union[str, None]
        output_data: Dict[str, str]

        files, dirs = lab.create_wildcards_lab()
        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, False)
        lab.remove_wildcards_lab(files, dirs)
        if minishell_out is None:
            return

        bash_output = sorted(bash_out.split())
        minishell_output = sorted(minishell_out.split())
        output_data = {
            "bash_out": bash_out,
            "minishell_out": minishell_out,
            "bash_file_content": None,
            "minishell_file_content": None,
            "bash_exit_status": None,
            "minishell_exit_status": None,
        }

        if all(elem in minishell_output for elem in bash_output)\
                and all(elem in bash_output for elem in minishell_output):
            self.printer.result("OK", loop, test, output_data=output_data)
        else:
            self.printer.result("KO", loop, test, output_data=output_data)
