#!/usr/bin/python3

"""
This module contains the `Process` class, which provides methods to
execute a command in a subprocess and interact with its input and output
streams.
"""

# Libraries ------------------------------------------------------------------>

import os
import pty
import re
import shutil
import signal
import subprocess
import threading
import time
from typing import List, Union

from printer import Printer

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# Functions ------------------------------------------------------------------>


class Process():
    """
    Attributes
    --------------------------------------------------------------------
    args : str
        The command to run.

    process : subprocess.Popen
        The Popen object representing the process.

    printer : Printer
        The Printer object used for logging.

    exit_status_bash : int
        The exit status of the bash process.

    exit_status_minishell : int
        The exit status of the minishell process.

    Methods
    --------------------------------------------------------------------
    get_bash_output():
        Runs a Bash command and returns its output as a string.

    get_minishell_output():
        It gets minishell output with subprocess.Popen().

    get_minishell_output_pty():
        It does the same thing as get_minishell_output() but uses the
        pty module to create a pseudo-tty and interact with it.
        This is because subprocess.Popen() does not correctly read
        the output when there are redirects or pipes in it.
    """

    def __init__(self, args: str, printer: Printer) -> None:

        self.args: str
        self.process: subprocess.Popen
        self.printer: Printer
        self.exit_status_bash: int
        self.exit_status_minishell: int

        self.args = args
        self.process: subprocess.Popen = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True,
        )
        self.printer = printer
        self.exit_status_bash = 0
        self.exit_status_minishell = 0

    def get_bash_output(self, test: str) -> str:
        """
        Runs a Bash command and returns its output as a string.

        Params
        ----------------------------------------------------------------
        test : str
            The command to run.

        Returns
        ----------------------------------------------------------------
        bash_output : str
            The output of the command executed in Bash.
        """
        bash_output: str

        bash_output = ""
        try:
            bash_output = subprocess.check_output(
                test,
                shell=True,
                executable=shutil.which("bash"),
                text=True,
                universal_newlines=True,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError as err:
            self.exit_status_bash = err.returncode

        return bash_output

    def get_minishell_output(self, bash_output: str, test: str, loop: int,
                             get_exit_status: bool) -> Union[str, None]:
        """
        It gets minishell output via a synchronization with bash output
        to avoid including the prompt or other garbage, but
        nevertheless, it is possible that not all cases are handled.
        It has been prefirmed to use write and read with write() and
        readlines() methods, as they allow more flexibility, than
        directly communicate(), although this requires more complex
        handling with threads since readlines() is subject to blocking.
        If the get_exit_status argument is True, it performs a recursion
        to get the output of "echo $?" on the same minishell instance.

        Params
        ----------------------------------------------------------------
        bash_output : str
            The output of the bash command.
        test : str
            The command to run.
        loop : int
            The number of times to loop.
        get_exit_status : bool
            Whether to get the exit status of the minishell process.

        Returns
        ----------------------------------------------------------------
        minishell_out : str
            The output of the command executed in minishell.
        """
        minishell_out: str
        counter: int
        tmp: List[str]

        def read_thread(self, tmp: list):

            line: str

            line = ""
            try:
                line = self.process.stdout.readline()
            except UnicodeError:
                line = "WARNING: Output is not UTF-8"
            if line:
                tmp.append(line)
            else:
                tmp.append("")
            return line

        try:
            minishell_out = ""
            counter = 0

            self.process.stdin.write(test + '\n')
            self.process.stdin.flush()

            while test not in minishell_out:
                tmp = []
                t = threading.Thread(target=read_thread, args=(self, tmp,))
                t.start()
                t.join(timeout=1)
                if t.is_alive():
                    raise subprocess.TimeoutExpired(self.process, 1)
                minishell_out += tmp[0]
                counter += 1

            minishell_out = ""
            counter = 0
            while minishell_out.count('\n') <= bash_output.count('\n'):
                if counter == bash_output.count('\n'):
                    break
                tmp = []
                t = threading.Thread(target=read_thread, args=(self, tmp,))
                t.start()
                t.join(timeout=1)
                if t.is_alive():
                    raise subprocess.TimeoutExpired(self.process, 1)
                minishell_out += tmp[0]
                counter += 1

            if get_exit_status:
                self.exit_status_minishell = int(self.get_minishell_output(
                    '\n', 'echo $?', loop, get_exit_status=False))
                if self.exit_status_minishell is None:
                    return None

            self.process.communicate(timeout=1)
            if self.process.returncode == -11:
                self.printer.result(
                    "KO", loop, test, excep="Segmentation fault")
                return None

        except subprocess.TimeoutExpired:
            self.process.send_signal(signal.SIGINT)
            self.printer.result("KO", loop, test, excep="Timeout")
            return None
        except Exception as err:
            if test != "echo $?":
                self.printer.result("KO", loop, test, excep=err)
            return None

        return minishell_out

    def get_minishell_output_pty(self, bash_output: str, test: str) -> str:
        """
        It does the same thing as get_minishell_output() but uses the
        pty module to create a pseudo-tty and interact with it.
        This is because subprocess.Popen() does not correctly read
        the output when there are redirects or pipes in it.

        Params
        ----------------------------------------------------------------
        bash_output : str
            The output of the bash command.
        test : str
            The command to run.

        Returns
        ----------------------------------------------------------------
        minishell_out : str
            The output of the command executed in minishell.
        """
        master: int
        slave: int
        process_pty: subprocess.Popen
        ansi_escape: re.Pattern
        minishell_out: str
        tmp: str

        master, slave = pty.openpty()
        process_pty = subprocess.Popen(
            self.args,
            stdin=slave,
            stdout=slave,
            stderr=slave,
            universal_newlines=True,
        )

        ansi_escape = re.compile(r'\x1b\[[0-9;]*[mK]')
        test += '\n'
        os.write(master, test.encode())
        time.sleep(0.5)
        tmp = ansi_escape.sub('', os.read(master, 1024).decode())
        tmp = tmp[tmp.find(test) + len(test):]
        tmp = tmp[tmp.find(test.strip('\n')) + len(test):]

        minishell_out = ""
        for line in tmp.split('\n'):
            if minishell_out.count('\n') == bash_output.count('\n') + 1:
                break
            minishell_out += line + '\n'
        minishell_out = minishell_out.strip('\n')
        minishell_out = minishell_out.replace('\r', '')
        minishell_out = minishell_out.replace('\x1b', '')
        minishell_out = minishell_out.replace('[?2004l', '')

        process_pty.kill()
        os.close(slave)
        os.close(master)

        return minishell_out
