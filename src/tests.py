#!/usr/bin/python3

"""
Arguments for testing.
"""

# Libraries ------------------------------------------------------------------>

from shutil import which
from typing import List

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Shkirov"
__license__ = "GPL-3.0"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Development"

# TESTS ---------------------------------------------------------------------->

parsing: List[str]
commands: List[str]
redirects: List[str]
pipes: List[str]
exit_status: List[str]
mix_mandatory: List[str]
booleans: List[str]
wildcards: List[str]
mix_bonus: List[str]

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
    "echo $",
    "echo '$'",
    "echo \"42\"'$'\"42\"",
    "echo a'b'c'd'e'f'g'h'i'j'k'l'm'n'o'p'q'r's't'",
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
    "echo \"$USER 42\" '\"$USER\"'",
    "echo $USER42",
    "echo ''\"\"'\"'\"'\"",
]

commands = [
    f"{which('ls')}",
    f"{which('ls')} -al",
    f"{which('ls')} -al -i",
    f"{which('ls')} -al -i -t",
    f"{which('ls')} -al -i -t -v",
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
    "wc -l /etc/passwd",
    "wc -l /etc/passwd -m",
    "wc -l /etc/passwd -m -w",
    "wc -l /etc/passwd -m -w -c",
    "wc -l /etc/passwd -m -w -c -l",
    "which ls",
    "which ls -al",
    "which ls -al -i",
    "which ls -al -i -t",
    "which ls -al -i -t -v",
    "which wc -l /etc/passwd",
    "which wc -l /etc/passwd -m",
    "which wc -l /etc/passwd -m -w",
    "which wc -l /etc/passwd -m -w -c",
    "which wc -l /etc/passwd -m -w -c -l",
]

redirects = [
    "< file1",
    "> file1",
    ">> file1",
    "< file1 > file2",
    "< file1 >> file2",
    "< file1 > file2 > file3 >> file4",
    "> file1 > file2 > file3 > file4",
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
    "cat /etc/passwd < /etc/passwd > file1",
    "cat /etc/passwd < /etc/passwd > file1 > file2",
    "cat /etc/passwd < /etc/passwd > file1 > file2 > file3",
    "cat file1 < /etc/passwd > file1 > file2 > file3",
    "cat file1 < /etc/passwd > file1 > file2 > file3 > file4",
    "cat file1 < /etc/passwd >> file1 >> file2",
    "cat file1 < /etc/passwd >> file1 >> file2 >> file3 >> file4",
]

pipes = [
    "ls / | grep etc",
    "ls / | grep etc | echo 42",
    "ls / | wc -l",
    "ls / | head -n 5",
    "ls -l / | grep home",
    "ls -l / | grep home | wc -l",
    "cat /etc/passwd | grep bash",
    "cat /etc/passwd | grep bash | wc -l",
    "echo \"Hello, World!\" | wc -w",
    "echo \"Hello, World!\" | sed 's/World/Universe/g'",
    "echo \"Hello, World!\" | cut -d \" \" -f 4",
    "echo \"Hello, World!\" | cut -d \" \" -f 4-6",
    "echo \"Hello, World!\" | cut -c 5-15",
    "ps -ef | grep apache | grep -v grep",
    "echo 1 | echo 2 | echo 3 | echo 4 | echo 5 | echo 6 | echo 7",
    "echo 1 | echo 2 | echo 3 | echo 4 | echo 42 | grep 2",
    "echo $SHELL | grep bash",
    "echo $LOGNAME | grep $LOGNAME",
    "echo \"$USER\" 42 \"'$SHELL'\" | grep bash | wc -l",
    "echo \"$USER\" 42 \"'$SHELL'\" | grep bash | wc -l | echo 42",
    "echo \"$USER\" 42 \"'$SHELL'\" | echo 42",
    "ls / | grep etc | echo 42 | ls / | grep etc | echo 42 | echo 21",
    "ls -al / | grep e | wc -l",
    "ls -al / | grep e | wc -l | echo 42",
    "ls -a -l / | wc -l",
    "echo '$USER' | grep $USER",
    "echo '$USER' | grep $USER | echo 42",
    "echo \"'$SHELL'\" | grep bash",
    "echo \"'$SHELL'\" | grep bash | grep b",
    "echo ''$USER'' | grep $USER",
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
    "| echo 1",
    "| echo 1 | echo 2",
    "ls not_existing_file",
    "ls not_existing_file | echo 42 | cat",
    "ls not_existing_file | cat > not_executable_file",
]

mix_mandatory = [
    "ls -al -i < /etc/passwd",
    "ls -al -i < /etc/passwd > file1",
    "ls -al -i < /etc/passwd > file1 > file2",
    "ls -al -i < /etc/passwd > file1 > file2 > file3",
    "ls -al -i < /etc/passwd > file1 > file2 > file3 > file4",
    "wc -l < /etc/passwd",
    "wc -l < /etc/passwd > file1 | wc -l",
    "wc -l < /etc/passwd > file1 > file2 > file3 > file4",
    "ls -al -i < /etc/passwd > file1 | wc -l | echo 42",
    "cat < file1 | cat > file2",
    "cat < file1 | grep 1 > file2 | wc -l",
    "cat < file1 | grep 1 > file2 | wc -l | echo 42",
    "cat < file1 | grep 1 > file2 | wc -l | echo 42 | echo 21",
    "> file1 | echo 42 | cat < file1 | grep 1 > file2 | wc -l",
    "< file1 | echo 42 > file2 | grep 1 | wc -l",
    "cat < file1 | cat > file2 < file1 | wc -l",
    "echo 42 > file1 | cat | wc -l",
    "echo 42 < file1 | cat | wc -l",
    ">> file1 | cat",
    ">> file1 | echo 42",
    "> file1 | cat < file1",
    "> file1 | echo 42 < file1 | cat file1",
    "echo 42 | wc -l | cat > file1",
    "echo 42 | cat | cat | cat | cat",
    "echo 42 | cat | cat | cat | cat | echo 21",
    "cat < file1 >> file2 > file1 | cat",
    "cat < file1 >> file2 > file1 | cat | echo 21",
    "ls / | grep c | cat > file1",
    "ls / | grep home | wc -l",
    "ls / | grep home | wc -l | < file1 > file2 | cat",
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
    "(echo 1 && echo 2) || ((echo 3 || echo 4) && (echo 5 || echo 6)) || "
    "(echo 7 && echo 8)",
    "echo 1 && (echo 2 || echo 3) && (echo 4 || (echo 5 && (echo 6 || echo 7 "
    "&& (echo 8 || (echo 9 && echo 10)))))",
    "echo 1 || (echo 2 || echo 3 || echo 4 || echo 5 || echo 6 || echo 7 || "
    "echo 8 || echo 9 || echo 10 || echo 11 || echo 12 || echo 13 || echo "
    "14 || echo 15 || echo 16 || echo 17 || echo 18 || echo 19 || echo 20)"
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
    "echo *~",
    "ls -al 42*42",
    "echo *1 *2 *3 *4 *5 *6 *7 *8 *9 *10 *11 *12 *13 *14 *15 *16 *17 *18 *19 ",
    "echo *1 file1 file2 directory1 directory2 *",
    "ls -al *1 file1 file2 directory1 directory2 *",
    "echo *1 file* f*2 d***ct*y* d*r*ory2 *2",
    "ls -al *1 file* f*2 d***ct*y* d*r*ory2 *2",
    "echo *1 file* f*2 d***ct*y* d*r*ory2 *2 *3 *4 *5 *6 *7 *8 *9 *10 *11 *12"
]

# mix_bonus = [
#     # "echo * | cat > file1",
#     # "echo * | cat > file1 | cat < file1",
#     # "echo * | cat > file1 | cat < file1 | cat > file2",
#     # "echo *** | cat > file1",
#     # "ls * | grep 1",
#     # "ls *** | grep 1",
#     # "ls *1 | grep file",
#     "(echo a && echo b) > file1",
#     "(echo a || echo b) > file1",
#     "(echo a && echo b || echo c && echo d) > file1",
#     "(((echo a || echo b) > file1) && echo c) | cat > file2 || echo d",
#     "echo file1 && ls not_dir | cat > file1",
#     "(echo file1 && ls not_dir) | cat > file1",
#     "(echo file1 && ls not_dir) | cat > file1 && echo 21 || echo 42",
#     "(echo f*l*********1 && ls not_dir) | cat > file1 && echo 21 || echo 42",
#     # "(((echo ***1 || ls not_dir) && cat < file1 | cat > file2 || ls ***",
#     # "echo *1 | cat > file1 && grep * | cat > file2 | cat < file2",
#     # "(echo a) | echo b",
#     "(echo a || echo b) | echo c",
#     "(echo a && echo b) | echo c || echo d && (echo e || echo f) | echo g",
#     "(cat < file1 || echo a) | (cat > file2 && echo b) > file3 | echo c",
# ]
