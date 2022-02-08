# tree

A minimal tree(1) implementation. 

Usage:

```
❯ python3 -m tree --help
usage: __main__.py [-h] [-e EXCLUDE_HIDDEN_FILES]

optional arguments:
  -h, --help            show this help message and exit
  -e EXCLUDE_HIDDEN_FILES, --exclude-hidden-files EXCLUDE_HIDDEN_FILES
```

For example:

```
❯ python3 -m tree -e .
.
┃  ┣━ __pycache__/
┃  ┃  ┣━ __init__.cpython-38.pyc
┃  ┃  ┗━ __main__.cpython-38.pyc
┃  ┣━ __init__.py
┃  ┗━ __main__.py
┣━ tests/
┃  ┣━ __init__.py
┃  ┗━ test_tree.py
┣━ README.md
┣━ pyproject.toml
┗━ LICENSE
```