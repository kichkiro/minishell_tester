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
        Remove the test lab.

    create_redirects_lab():
        Creates 4 temporary files in the Lab's directory and returns 
        their paths as a tuple.

    remove_redirects_lab():
        Removes the specified files from the Lab's directory.

    create_exit_status_lab():
        Creates a file in the Lab's directory and returns its path.

    remove_exit_status_lab():
        Removes the specified file.

    create_wildcard_lab():
        Creates two files and two directories at the root of the Lab's
        and two files for each directory, and returns their paths as a
        tuple.

    remove_wildcard_lab():
        Removes the specified files and drirectories.

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


    def remove_redirects_lab(self, files:list) -> None:

        for file in files:
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


    def create_wildcards_lab(self) -> tuple:
        filenames = ["file1", "file2"]
        dirnames = ["directory1", "directory2"]

        for i, filename in enumerate(filenames):
            filepath = os.path.join(".", filename)
            with open(filepath, "w") as f:
                f.write(str(i+1))

        for dirname in dirnames:
            os.makedirs(dirname)
            for i, filename in enumerate(filenames):
                filepath = os.path.join(dirname, filename)
                with open(filepath, "w") as f:
                    f.write(str(i+1))

        return (filenames, dirnames)


    def remove_wildcards_lab(self, filenames:list, dirnames:list) -> None:

        for dirname in dirnames:
            shutil.rmtree(dirname)

        for filename in filenames:
            if os.path.exists(filename):
                os.remove(filename)
