### Hexlet tests and linter status:
[![Actions Status](https://github.com/averyanovalex/python-project-lvl2/workflows/hexlet-check/badge.svg)](https://github.com/averyanovalex/python-project-lvl2/actions)
[![example workflow](https://github.com/averyanovalex/python-project-lvl2/actions/workflows/ci.yml/badge.svg)](https://github.com/averyanovalex/python-project-lvl2/actions/workflows/ci.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/fe5aebec8abc8f6154c7/maintainability)](https://codeclimate.com/github/averyanovalex/python-project-lvl2/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/fe5aebec8abc8f6154c7/test_coverage)](https://codeclimate.com/github/averyanovalex/python-project-lvl2/test_coverage)


# Training project "Difference generator" on hexlet.io

## Links

This project was built using these tools:

| Tool                                                                        | Description                                        |
|-----------------------------------------------------------------------------|----------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management packaging made easy" |

##  Install

To install project:

1.Install Poetry (instruction: `https://poetry.eustace.io/`)

2.Clone repository:

`git clone git@github.com:averyanovalex/python-project-lvl1.git`

3.Install dependencies:

`poetry install` (or `make install`)

4.Build and install package:

`poetry build` (or `make build`)

`python3 -m pip install --user dist/*.whl` (or `make package-install`)

5.Run game:

`gendiff file1 file2 [--format stylish | --format json | --format plain]`

or see how it works.

## How it works
### diff json files (format: stylish)
[![asciicast](https://asciinema.org/a/tYKB33ydwG1KVI1MQL78yNkx7.svg)](https://asciinema.org/a/tYKB33ydwG1KVI1MQL78yNkx7)

### diff yaml files (format: stylish)
[![asciicast](https://asciinema.org/a/lgdulDWM39LJJjfgLcb6rr3VZ.svg)](https://asciinema.org/a/lgdulDWM39LJJjfgLcb6rr3VZ)

### diff multi-level json files (format: stylish)
[![asciicast](https://asciinema.org/a/Xs7fNjY5rxT1jyTFO9TK8OQxd.svg)](https://asciinema.org/a/Xs7fNjY5rxT1jyTFO9TK8OQxd)

### diff multi-levell json files (format: plain)
[![asciicast](https://asciinema.org/a/ZGFlqDg5TnqtK07YTKgJs0V3b.svg)](https://asciinema.org/a/ZGFlqDg5TnqtK07YTKgJs0V3b)

### diff multi-level json files (format: json)
[![asciicast](https://asciinema.org/a/stSYVA4PPSTNTSqaTG7l6wEGN.svg)](https://asciinema.org/a/stSYVA4PPSTNTSqaTG7l6wEGN)
