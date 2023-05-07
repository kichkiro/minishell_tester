#!/usr/bin/python3

"""
Arguments for testing.
"""

# Libraries ------------------------------------------------------------------>

from shutil import which

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# TESTS ---------------------------------------------------------------------->

parsing = [
    "echo ",
    "echo hello world !",
    "echo 42test ' 21 '",
    "echo 42   42    '  '42",
    "echo 'echo $v >> file.txt'",
    "echo ' \"\" ' '42'",
	"echo '$?'",
    "echo '${$?}'",
    "echo 42' '42",
    "echo '$USER'",
    "echo '<< | | >>'42",
    "echo ''",
    "echo ''''42''",
    "echo $'USER'",
    "echo $'USER'USER",
    "echo a'b'c'd'e'f'g'h'i'j'k'l'm'n'o'p'q'r's't'",
    "echo a'b'c'd'e'f'g'h'i'j'k'l'm''",
    "echo \" \"'$USER\"'\"42 \" ''\"  | << -1\"",
    "echo \"<< EOF\"",
    "echo $HOME",
    "echo $HOME$HOME",
    "echo $USER'$USER'",
    "echo $USER \"$HOME\"",
    "echo $USER42",
    "echo '$USER \"$HOME\"'",
    "echo $USER '>> file.txt' \"|\"",
    "echo '42 $USER' \">\" file.txt",
    "echo \"$USER 42\" '\"$USER\"'" ,
    "echo $USER42",
    "echo ''\"\"'\"'\"'\"",
]

commands = [
    f"{which('ls')}",
    f"{which('ls')} -al",
    f"{which('ls')} -al -i",
    f"{which('ls')} -al -i -t",
    f"{which('ls')} -al -i -t -v",
    f"{which('cat')} /etc/passwd",
    f"{which('cat')} /etc/passwd -n",
    f"{which('cat')} /etc/passwd -n -e",
    f"{which('cat')} /etc/passwd -n -e -t",
    f"{which('cat')} /etc/passwd -n -e -t -v",
    f"{which('wc')} -l /etc/passwd",
    f"{which('wc')} -l /etc/passwd -m",
    f"{which('wc')} -l /etc/passwd -m -w",
    f"{which('wc')} -l /etc/passwd -m -w -c",
    f"{which('wc')} -l /etc/passwd -m -w -c -l",
    "ls",
    "ls -al",
    "ls -al -i",
    "ls -al -i -t",
    "ls -al -i -t -v",
    "cat /etc/passwd",
    "cat /etc/passwd -n",
    "cat /etc/passwd -n -e",
    "cat /etc/passwd -n -e -t",
    "cat /etc/passwd -n -e -t -v",
    "wc -l /etc/passwd",
    "wc -l /etc/passwd -m",
    "wc -l /etc/passwd -m -w",
    "wc -l /etc/passwd -m -w -c",
    "wc -l /etc/passwd -m -w -c -l",
]

redirects = [
    "< file1",
    "> file1",
    ">> file1",
    "< file1 > file2",
    "< file1 >> file2",
    "cat < file1",
    "cat < file1 > file2 > file3",
    "cat < file1 >> file2 >> file3",
    "cat < file1 >> file2 > file3",
    "cat < file1 > file2 >> file3",
    "cat < file1 < file2",
    "cat < file1 < file2 < file3 < file4",
    "cat < file1 < file2 > file3 >> file4",
    "cat < file1 < file2 > file3 > file4",
    "cat < file1 >> file2 >> file3 < file4",
    "cat < file1 > file2 < file3",
    "cat > file1 < file2",
    "cat >> file1 < file2 < file3",
    "cat >> file1 > file2 < file3 < file4",
    "cat >> file1 >> file2 < file3 < file4",
    "cat >> file1 >> file2 >> file3 < file4",
    "cat /etc/passwd < /etc/passwd",
    "cat /etc/passwd < /etc/passwd > file1",
    "cat /etc/passwd < /etc/passwd > file1 > file2",
    "cat /etc/passwd < /etc/passwd > file1 > file2 > file3",
    "cat file1 < /etc/passwd > file1 > file2 > file3",
    "cat file1 < /etc/passwd > file1 > file2 > file3 > file4",
    "cat file1 < /etc/passwd >> file1 >> file2",
    "cat file1 < /etc/passwd >> file1 >> file2 >> file3",
    "cat file1 < /etc/passwd >> file1 >> file2 >> file3 >> file4",
]

exit_status = [
    "echo 42",
    "cat 42 > not_executable_file",
    "cat 42 > not_existing_file",
    "./not_executable_file",
    "not_existing_command",
    "< not_existing_file",
    "> not_existing_file",
    ">> not_existing_file",
    "< not_existing_file > not_existing_file2",
    "< not_existing_file >> not_existing_file2",
    # "| echo 1"
    # "| echo 1 | echo 2",
]

mixed = [
    "ls -al -i < /etc/passwd",
    "ls -al -i < /etc/passwd > file1",
    "ls -al -i < /etc/passwd > file1 > file2",
    "ls -al -i < /etc/passwd > file1 > file2 > file3",
    "ls -al -i < /etc/passwd > file1 > file2 > file3 > file4",
    "wc -l < /etc/passwd > file1 > file2 > file3 > file4",
    "wc -l < /etc/passwd",
    "wc -l < /etc/passwd",
]

booleans = [
    "echo 42 && echo 21",
    "echo 42 || echo 21",
    "42 && echo 21",
    "42 || echo 21",
    "echo 1 && echo 2 && echo 3 && echo 4 && echo 5",
    "echo 1 && (echo 2 && echo 3)",
    "echo 1 && (echo 2 || echo 3) && echo 4",
    "1 || 2 || 3 || 4 || echo 5",
    "echo 1 || (echo 2 && echo 3) || echo 4",
    "echo 1 && (echo 2 || echo 3) && echo 4 && (echo 5 || echo 6)",
    "(echo 1 && echo 2) || (echo 3 && echo 4) && (echo 5 || echo 6)",
    "((((echo 1 || (echo 2 || 3) && echo 4) || echo 5) && echo 6) || echo 7)",
    "1 || (echo 2 && ((echo 3 || echo 4) && echo 5))",
    "1 || (echo 2 && ((3 || echo 4) || echo 5))",
    "((echo 1 && echo 2) || (echo 3 && echo 4))",
    "(echo 1 && echo 2) || (echo 3 && echo 4)",
    "(echo 1 && echo 2) || echo 3",
    "echo 1 || (echo 2 && echo 3) && echo 4",
    "(echo 1 || echo 2) && (echo 3 || echo 4)",
    "echo 1 && (echo 2 || echo 3) || echo 4",
    "(echo 1 && echo 2) && (echo 3 || echo 4)",
    "(echo 1 || echo 2) && (echo 3 || echo 4) && (echo 5 || echo 6)",
    "(echo 1 && echo 2) || (echo 3 || echo 4) || (echo 5 && echo 6)",
    "(echo 1 || echo 2) && (echo 3 || echo 4) || (echo 5 && echo 6)",
    "(echo 1 || echo 2) && echo 3 || echo 4",
    "echo 1 && (echo 2 || echo 3) && () && echo 4",
    "((echo 1 && echo 2) || (echo 3 || echo 4)) && (echo 5 && echo 6)",
    "(echo 1 && echo 2) || ((echo 3 || echo 4) && (echo 5 || echo 6)) || \
        (echo 7 && echo 8)",
    "echo 1 && (echo 2 || echo 3) && (echo 4 || (echo 5 && (echo 6 || echo 7 \
        && (echo 8 || (echo 9 && echo 10)))))",
    "echo 1 || (echo 2 || echo 3 || echo 4 || echo 5 || echo 6 || echo 7 || \
        echo 8 || echo 9 || echo 10 || echo 11 || echo 12 || echo 13 || echo \
        14 || echo 15 || echo 16 || echo 17 || echo 18 || echo 19 || echo 20)",
]

wildcards = [
    "echo *",
    "ls *",
    "ls -al *",
    "echo $USER*",
    "echo i*l*de",
    "echo ***y",
    "echo d*************************y",
    "echo **************1",
    "ls -al d*cto*r*1",
    "ls -al d*cto*r*1*",
    "echo ****1 ***2",
    "ls -al file*",
    "ls -al directory*",
    "ls -al *1",
    "ls -al *2",
    "echo d*y",
    "echo *i*e*",
    "echo *1 *2",
    "echo d*2",
    "echo **1**",
    "echo d*fi*",
    "echo *42 *21",


    

]
