#!/usr/bin/python3

"""
A class to run a set of tests on a given project and evaluate the 
results.
"""

# Libraries ------------------------------------------------------------------>

import os
from subprocess import Popen

from termcolor import colored
import tests
from lab import Lab
from process import Process
from printer import Printer

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# Functions ------------------------------------------------------------------>

class Tester:
    """
    Attributes
    --------------------------------------------------------------------
    project_path : str
        The path to the project to be tested.

    test : str
        The name of the test to run.

    Methods
    --------------------------------------------------------------------
    run():
        Runs the test cases and prints the results.

    ...

    Notes
    --------------------------------------------------------------------
    The Tester class is designed to run tests on a project executable. 
    The test cases are run using subprocess.Popen, which allows for 
    running external programs and capturing their output.
    """
    
    def __init__(self, project_path:str, exe:str, test:str, printer:Printer) \
        -> None:

        self.project_path = project_path
        self.printer = printer
        if test == "parsing":
            self.name = "parsing"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.parsing
            self.tester = self.__commands
        elif test == "commands":
            self.name = "commands"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.commands
            self.tester = self.__commands
        elif test == "redirects":
            self.name = "redirects"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.redirects
            self.tester = self.__redirects
        elif test == "exit_status":
            self.name = "exit_status"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.exit_status
            self.tester = self.__exit_status


    def run(self) -> None:

        loop = 0
        for test in self.tests:
            lab = Lab(self.name)
            os.chdir(lab.path)
            process = Process(self.cmd, self.printer)
            try:
                if self.name == "parsing":
                    self.tester(process, test, loop)
                elif self.name == "commands":
                    self.tester(process, test, loop)
                elif self.name == "redirects":
                    self.tester(process, test, loop, lab)
                elif self.name == "exit_status":
                    self.tester(process, test, loop, lab)
            except Exception as e:
                print(colored(f"Exception: {e}", "red"))
            finally:
                lab.remove()
                loop += 1
    

    def __commands(self, process: Popen, test: str, loop: int) -> None:

        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, False)
        if minishell_out == None:
            return
        bash_out = bash_out.strip('\n')
        minishell_out = minishell_out.strip('\n')

        if minishell_out == bash_out or minishell_out[:-1] == \
            bash_out:
            self.printer.result("OK", loop, test, bash_out, minishell_out)
        else:
            self.printer.result("KO", loop, test, bash_out, minishell_out)


    def __redirects(self, process:Popen, test:str, loop:int, lab:Lab) -> None:
        
        test_files = lab.create_redirects_lab()
        bash_out = process.get_bash_output(test)
        bash_file_content = {}
        for file in test_files:
            with open(file, 'r') as f:
                bash_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)
        
        test_files = lab.create_redirects_lab()
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, False)
        if minishell_out == None:
            return
        minishell_file_content = {}        
        for file in test_files:
            with open(file, 'r') as f:
                minishell_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)

        bash_out = bash_out.strip('\n')
        minishell_out = minishell_out.strip('\n')

        if (minishell_out == bash_out or minishell_out[:-1] == \
            bash_out) and minishell_file_content == bash_file_content:
           self.printer.result("OK", loop, test, bash_out, minishell_out,
                bash_file_content, minishell_file_content)
        else:
            self.printer.result("KO", loop, test, bash_out, 
                minishell_out, bash_file_content, minishell_file_content)


    def __exit_status(self, process:Popen, test:str, loop:int, lab:Lab) -> None:

        file = lab.create_exit_status_lab()
        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(bash_out, test, loop, True)
        lab.remove_exit_status_lab(file)
        if minishell_out == None:
            return

        if process.exit_status_bash == process.exit_status_minishell:
            self.printer.result("OK", loop, test, 
                bash_exit_status=process.exit_status_bash,
                minishell_exit_status=process.exit_status_minishell)
        else:
            self.printer.result("KO", loop, test,
                bash_exit_status=process.exit_status_bash,
                minishell_exit_status=process.exit_status_minishell)
