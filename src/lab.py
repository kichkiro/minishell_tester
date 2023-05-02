#!/usr/bin/python3

"""

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
    """
    def __init__(self, test: str) -> None:

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


    def remove_redirects_lab(self, test_files) -> None:

        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
