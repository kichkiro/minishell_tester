#!/usr/bin/python3

"""
A class to run a set of tests on a given project and evaluate the 
results.
"""

# Libraries ------------------------------------------------------------------>

import os
import signal
import subprocess

from termcolor import colored
import tests
from lab import Lab
from process import Process

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
    
    def __init__(self, project_path: str, exe: str, test: str) -> None:

        self.project_path = project_path
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


    def run(self) -> None:

        counter = 0
        for test in self.tests:
            lab = Lab(self.name)
            os.chdir(lab.path)
            process = Process(self.cmd)
            try:
                if self.name == "echo":
                    self.tester(process, test, counter)
                elif self.name == "redirects":
                    self.tester(process, test, counter, lab)
            except Exception as e:
                print(colored(f"Exception: {e}", "red"))
            finally:
                lab.remove()
                counter += 1

    
    def __echo(self, process: subprocess.Popen, test: str, counter: int) \
        -> None:

        def print_result(status, bash_output, minishell_output):
            if status == "OK":
                color = "green"
                print(colored(
                    f"TEST {counter + 1}: {status}\n",
                    color
                ))
            else:
                color = "red"
                print(colored(
                    f"TEST {counter + 1}: {status}\n"
                    f"    Input:     {test}\n"
                    f"    Bash:      {bash_output}\n"
                    f"    Minishell: {minishell_output}\n",
                    color
                ))

        bash_output = process.get_bash_output(test)
        minishell_output = process.get_minishell_output(
            bash_output, test, counter)[0]
        bash_output = bash_output.strip('\n')
        minishell_output = minishell_output.strip('\n')

        if minishell_output == bash_output or minishell_output[:-1] == \
            bash_output:
            print_result("OK", bash_output, minishell_output)
        else:
            print_result("KO", bash_output, minishell_output)
    

    def __redirects(self, process: subprocess.Popen, test: str, counter: int, \
        lab: Lab) -> None:

        def print_result(status, bash_output, minishell_output, \
            bash_file_content, minishell_file_content):

            if status == "OK":
                color = "green"
                print(colored(
                    f"TEST {counter + 1}: {status}\n",
                    color
                ))
            else:
                color = "red" 
                print(colored(
                    f"TEST {counter + 1}: {status}\n"
                    f"    Input:     {test}\n"
                    f"    Bash:      {bash_output}\n"
                    f"    Minishell: {minishell_output}\n\n"
                    f"    Files content BASH:",
                    color
                ))
                for key, value in bash_file_content.items():
                    print(colored(
                        f"      {key}: {value}",
                        color
                    ))
                print(colored("\n    Files content MINISHELL:", color))
                for key, value in minishell_file_content.items():
                    print(colored(
                        f"      {key}: {value}",
                        color
                    ))
                print()
        
        test_files = lab.create_redirects_lab()
        bash_output = process.get_bash_output(test)
        bash_file_content = {}
        for file in test_files:
            with open(file, 'r') as f:
                bash_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)
        
        test_files = lab.create_redirects_lab()
        minishell_output = process.get_minishell_output(
            bash_output, test, counter)[0]
        minishell_file_content = {}        
        for file in test_files:
            with open(file, 'r') as f:
                minishell_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)

        bash_output = bash_output.strip('\n')
        minishell_output = minishell_output.strip('\n')

        if (minishell_output == bash_output or minishell_output[:-1] == \
            bash_output) and minishell_file_content == bash_file_content:
            print_result("OK", bash_output, minishell_output,\
                bash_file_content, minishell_file_content)
        else:
            print_result("KO", bash_output, minishell_output,\
                bash_file_content, minishell_file_content)
