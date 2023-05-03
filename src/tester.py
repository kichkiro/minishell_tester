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

    Private Methods
    ---------------
    __echo(...) <- DOCUMENT FROM HERE ******************

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
        if test == "echo":
            self.name = "echo"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.echo
            self.tester = self.__echo
        elif test == "redirects":
            self.name = "redirects"
            self.cmd = ([f"{project_path}/{exe}"])
            self.tests = tests.redirect
            self.tester = self.__redirects
        # elif test == "heredoc":
        #     self.name = "heredoc"
        #     self.cmd = ([f"{project_path}/{exe}"])
        #     self.tests = tests.heredoc
        #     self.tester = self.__heredoc


    def run(self) -> None:

        loop = 0
        for test in self.tests:
            lab = Lab(self.name)
            os.chdir(lab.path)
            process = Process(self.cmd, self.printer)
            try:
                if self.name == "echo":
                    self.tester(process, test, loop)
                elif self.name == "redirects":
                    self.tester(process, test, loop, lab)
                # elif self.name == "heredoc":
                #     self.tester(process, test, loop, lab)
            except Exception as e:
                print(colored(f"Exception: {e}", "red"))
            finally:
                lab.remove()
                loop += 1

    
    def __echo(self, process:Popen, test: str, loop:int) -> None:

        bash_output = process.get_bash_output(test)
        minishell_output = process.get_minishell_output(
            bash_output, test, loop, True)
        if minishell_output == None:
            return
        
        bash_output = bash_output.strip('\n')
        minishell_output = minishell_output.strip('\n')

        if minishell_output == bash_output or minishell_output[:-1] == \
            bash_output:
            self.printer.result("OK", loop, test, bash_output, minishell_output)
        else:
            self.printer.result("KO", loop, test, bash_output, minishell_output)
    

    def __redirects(self, process:Popen, test:str, loop:int, lab:Lab) -> None:
        
        test_files = lab.create_redirects_lab()
        bash_output = process.get_bash_output(test)
        bash_file_content = {}
        for file in test_files:
            with open(file, 'r') as f:
                bash_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)
        
        test_files = lab.create_redirects_lab()
        minishell_output = process.get_minishell_output(
            bash_output, test, loop, True)
        minishell_file_content = {}        
        for file in test_files:
            with open(file, 'r') as f:
                minishell_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)

        bash_output = bash_output.strip('\n')
        minishell_output = minishell_output.strip('\n')

        if (minishell_output == bash_output or minishell_output[:-1] == \
            bash_output) and minishell_file_content == bash_file_content:
           self.printer.result("OK", loop, test, bash_output, minishell_output,
                bash_file_content, minishell_file_content)
        else:
            self.printer.result("KO", loop, test, bash_output, 
                minishell_output, bash_file_content, minishell_file_content)


    # def __heredoc(self, process: Popen, test: str, loop: int, lab: Lab) -> None:

    #     test_files = lab.create_redirects_lab()
    #     bash_output = process.get_bash_output(test)
    #     bash_file_content = {}
    #     for file in test_files:
    #         with open(file, 'r') as f:
    #             bash_file_content[file[-5:]] = f.read()
    #     lab.remove_redirects_lab(test_files)

    #     test_files = lab.create_redirects_lab()
    #     minishell_file_content = {}
    #     for file in test_files:
    #         with open(file, 'r') as f:
    #             minishell_file_content[file[-5:]] = f.read()
    #     process.get_minishell_output(bash_output, test, loop, False)
    #     minishell_file_content = {}        
    #     for file in test_files:
    #         with open(file, 'r') as f:
    #             minishell_file_content[file[-5:]] = f.read()
    #     lab.remove_redirects_lab(test_files)

    #     if minishell_file_content == bash_file_content:
    #         self.printer.result(
    #             "OK", loop, test, bash_file_content=bash_file_content, 
    #             minishell_file_content=minishell_file_content
    #         )
    #     else:
    #         self.printer.result(
    #             "KO", loop, test, bash_file_content=bash_file_content, 
    #             minishell_file_content=minishell_file_content
    #         )
