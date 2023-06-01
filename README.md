# Minishell Tester

<img src="https://github.com/kichkiro/42_cursus/blob/assets/minishell_tester_usage.gif?raw=true" width="100%"/>


## 🐍 - Python
```bash
python3 --version >= Python 3.8
```

## 🛠️ - How to use?

#### First time
```bash
git clone https://github.com/kichkiro/minishell_tester.git
cd minishell_tester 
pip3 install -r requirements.txt 
python3 src/__main__.py [project path]
```

#### Next times
```bash
python3 src/__main__.py [project path]
```

## 📈 - Tester

The tests are divided into the following categories:
- Parsing
- Commands
- Redirects
- Pipe
- Exit status
- Booleans
- Wildcards

IMPORTANT: The tests are not exhaustive, so it is possible that the project is not 100% functional even if all the tests are passed. Make your own tests.

## 📝 - Compatibility

As much as I have tried to make the tester as generic as possible, there may be some projects that may not be compatible. In that I have noticed that the Popen() method of the 'subprocess' module, the method I use to capture minishell output for some tests (Parsing, Commands, Exit Status, Booleans, Wildcards), does not always return the correct output on all projects.

## 🪲 - Report bugs
To report bugs, contact me:
- Slack: <b>kichkiro</b>
- E-Mail: <b>kichkiro@student.42firenze.it</b>

Also feel free to send me Pull Request to add tests, implement new features, or fix bugs.

## ⚖️ - License
See [LICENSE](LICENSE)
