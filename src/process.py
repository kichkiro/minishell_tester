#!/usr/bin/python3

"""

"""

# Libraries ------------------------------------------------------------------>

import signal
import shutil
import threading
import subprocess

from printer import Printer

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# Functions ------------------------------------------------------------------>

class Process():
    """
    """
    def __init__(self, args:str, printer:Printer) -> None:
        self.process = subprocess.Popen(
            args,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            universal_newlines=True,   
        )
        self.printer = printer
        # self.lock = threading.Lock()


    def get_bash_output(self, input:str) -> str:
        
        bash_output = subprocess.check_output(
            input,
            shell=True,
            executable=shutil.which("bash"),
            text=True,
            universal_newlines=True
        )
        return bash_output


    def get_minishell_output(self, bash_output:str, input:str, loop:int, \
        get_output:bool) -> tuple:

        def read_thread(self, tmp:list):
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

            self.process.stdin.write(input + '\n')
            self.process.stdin.flush()

            if get_output:
                while input not in minishell_out:
                    minishell_out += self.process.stdout.readline()
                minishell_out = ""
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

            self.process.communicate(timeout=1)
            if self.process.returncode == -11:
                self.printer.result(
                    "KO", loop, input, exception="Segmentation fault")
                return None

        except subprocess.TimeoutExpired:
            self.process.send_signal(signal.SIGINT)
            self.printer.result("KO", loop, input, exception="Timeout")
            return None
        except Exception as e:
            self.printer.result("KO", loop, input, exception=e)
            return None

        return minishell_out
