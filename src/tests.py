#!/usr/bin/python3

"""
Arguments for testing.
"""

# Authorship ----------------------------------------------------------------->

__author__ = "Kirill Chkirov"
__license__ = "other"
__email__ = "kichkiro@student.42firenze.it"
__slack__ = "kichkiro"
__status__ = "Prototype"

# TESTS ---------------------------------------------------------------------->

echo = [
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

redirect = [
    "echo 42 < file1",
    "< file1",
    "> file1",
    ">> file1",
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
]

heredoc = [
    # "cat << \"E OF>\"file1",
    # "cat << \"E OF\"",
    # "cat << \"\"E\"O\"F\"\"",
    # "cat << ''EOF''",
    # "cat << '''E'O'F'''",
    # "cat << \"\"E\"O\"F\"\"",
    # "cat << \"EOF\"\"\"",

    "<< EOF\nEOF",    
    "< file1 < file2 < file3 << EOF\n42\nEOF",
    "cat < file1 > file2 << EOF\n42\nEOF",
    "cat < file1 > file2 << EOF > file3 << EOF\n42\nEOF\n43\nEOF",
    "cat << EOF > file1 << EOF\n42\nEOF\n43\nEOF"
    
]
