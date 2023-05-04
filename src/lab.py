#!/usr/bin/python3

"""
This module defines a Lab class which is responsible for creating and 
removing temporary directories used during testing.
"""

# Libraries ------------------------------------------------------------------>

import os
import shutil
import tempfile

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# Functions ------------------------------------------------------------------>

class Lab:
    """
     Attributes
    --------------------------------------------------------------------
    test_name : str 
        The name of the test.

    path : str
        Path of the test lab.

    Methods
    --------------------------------------------------------------------
    remove():
        Removes the temporary directory.

    create_redirects_lab():
        Creates 4 temporary files in the Lab's directory and returns 
        their paths as a tuple.

    remove_redirects_lab():
        Removes the specified files from the Lab's directory.

    """
    def __init__(self, test:str) -> None:

        self.test_name = test
        self.path = tempfile.mkdtemp()


    def remove(self):

        shutil.rmtree(self.path)


    def create_redirects_lab(self) -> tuple:

        filenames = ["file1", "file2", "file3", "file4"]
        paths = [os.path.join(self.path, filename) for filename in filenames]
        contents = [filename[-1] + '\n' for filename in filenames]

        for path, content in zip(paths, contents):
            with open(path, 'w') as file:
                file.write(content)

        return tuple(paths)


    def remove_redirects_lab(self, test_files:list) -> None:

        for file in test_files:
            if os.path.exists(file):
                os.remove(file)


    def create_exit_status_lab(self) -> str:

        path = os.path.join(self.path, "not_executable_file")
        with open(path, 'w') as file:
            file.write("42")

        return path
    

    def remove_exit_status_lab(self, path:str) -> None:

        if os.path.exists(path):
            os.remove(path)
