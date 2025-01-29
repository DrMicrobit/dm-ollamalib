# dm-ollama

Python package: helper functions to parse Ollama options from a string. Also show available options.

Nothing stellar, but these functionalities are somehow missing from the Ollama Python package.

# Installation
## Installation via PyPi
Not yet, TBD
## Installation from source
TBD
## Installation via 'uv'
Simply do `uv add git+https://github.com/DrMicrobit/dm-ollamalib` and you are good to go.

# Usage examples

```python
from dm_ollamalib.parse_options import help_long, help_overview, to_ollama_options

print(help_overview())
print(help_long())

print(to_ollama_options("top_p=0.9;temperature=0.8"))
print(to_ollama_options(["top_p=0.9", "temperature=0.8"]))
```

The first two lines will print the generated help texts for the options present in the Ollama Python package. The two subsequent lines show how to parse options from one or several strings coming from, e.g. command line.

The dictionary returned by `to_ollama_options()` can be used directly in calls to Ollama. E.g.

```python
import ollama
from dm_ollamalib.optionhelper import to_ollama_options

op = to_ollama_options("top_p=0.9;temperature=0.8")
ostream = ollama.chat(
    model="llama3.1",
    options=op,
    ...
)
```


# Notes
The GitHub repository comes with all files I currently use for Python development across multiple platforms. Notably:

- configuration of the Python environment via `uv`: pyproject.toml and uv.lock
- configuration for linter and code formatter `ruff`: ruff.toml
- configuration for `pylint`: .pylintrc
- git ignore files: .gitignore
- configuration for `pre-commit`: .pre-commit-config.yaml. The script used to check `git commit` summary message is in devsupport/check_commitsummary.py
- configuration for VSCode editor: .vscode directory
