#!/usr/bin/python3

"""
A class to run a set of tests on a given project and evaluate the 
results.
"""

# Libraries ------------------------------------------------------------------>

import os
from typing import List, Union

from termcolor import colored
import tests
from lab import Lab
from process import Process
from printer import Printer

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

    __exec():
        Executes a test case using the provided process object, test 
        name, and loop index.
        Compares the output of the test case in both Bash and Minishell 
        and prints the result.

    __exec2():
        Executes a test case using the provided process object, 
        test name, loop index, and lab object.
        Compares the output and file contents of the test case in both 
        Bash and Minishell and prints the result.

    __exitstatus():
        Executes a test case to check the exit status using the provided 
        process object, test name, loop index, and lab object.
        Compares the exit status of the test case in both Bash and 
        Minishell and prints the result.

    __wildcards():
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
    
    def __init__(self, project_path:str, exe:str, test:str, printer:Printer) \
        -> None:

        self.name:str
        self.project_path:str
        self.cmd:str
        self.printer:Printer
        self.tests:List[str]

        self.name = test
        self.project_path = project_path
        self.cmd = f"{project_path}/{exe}"
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

        loop:int
        test:str
        lab:Lab
        process:Process

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
            except Exception as e:
                print(colored(f"Exception: {e}", "red"))
            finally:
                lab.remove()
                loop += 1
    

    def __exec(self, process:Process, test:str, loop:int) -> None:

        bash_out:str
        minishell_out:Union[str,None]

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


    def __exec2(self, process:Process, test:str, loop:int, lab:Lab) -> None:

        test_files:List[str]
        bash_out:str
        minishell_out:str
        bash_file_content:dict
        minishell_file_content:dict

        test_files = lab.create_redirects_lab()
        bash_out = process.get_bash_output(test)
        bash_file_content = {}
        for file in test_files:
            with open(file, 'r') as f:
                bash_file_content[file[-5:]] = f.read()
        lab.remove_redirects_lab(test_files)
        
        test_files = lab.create_redirects_lab()
        minishell_out = process.get_minishell_output_pty(
            bash_out, test, loop)
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


    def __exitstatus(self, process:Process, test:str, loop:int, lab:Lab)\
        -> None:

        file:str
        bash_out:str
        minishell_out:Union[str,None]

        file = lab.create_exit_status_lab()
        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, True)
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


    def __wildcards(self, process:Process, test:str, loop:int, lab:Lab)\
        -> None:
        
        files:List[str]
        dirs:List[str]
        bash_out:str
        minishell_out:Union[str,None]

        files, dirs = lab.create_wildcards_lab()
        bash_out = process.get_bash_output(test)
        minishell_out = process.get_minishell_output(
            bash_out, test, loop, False)
        lab.remove_wildcards_lab(files, dirs)
        if minishell_out == None:
            return
        bash_output = sorted(bash_out.split())
        minishell_output = sorted(minishell_out.split())

        if all(elem in minishell_output for elem in bash_output) and \
            all(elem in bash_output for elem in minishell_output):
            self.printer.result("OK", loop, test, bash_out, minishell_out)
        else:
            self.printer.result("KO", loop, test, bash_out, minishell_out)
