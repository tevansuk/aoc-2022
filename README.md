# 2021 Advent of Code Python template

This is a small python project to automate setting up each days challenges.

It also contains my solutions for the 2021 challenge on the branch `tom`

## Creating stubs for a day

Run `poetry run mkday N`. This will create the following files (eg for day 5):

* `aoc/five.py`
* `tests/test_five.py`
* `tests/five.txt`

If you have `EDITOR=vim` in your environment, it will also open those files.

Paste the days sample input in to the test data file, and then save your personal days' input to `resources/five.txt`

The days stubs will look like this:

```python
from dataclasses import dataclass
from pathlib import Path


def main(datafile: Path):
    data = parse_data(datafile)
    print(f"Q1: {data}")
    print(f"Q2: {data}")


def parse_data(datafile: Path):
    with datafile.open() as fp:
        return [line for line in fp.readlines()]
```

```python
from pathlib import Path

import pytest

from aoc.five import *


@pytest.fixture
def data():
    return parse_data(Path(__file__).parent / "five.txt")


def test_parse_data(data):
    assert len(data) == 0
```

## Running a day's code

To run your code, run `poetry run day N`. This will call the `main` method in
that days module, with the path to that days input as the argument.

To run the test code, run `poetry run pytest`.

To run mypy static type checking, run `poetry run mypy`.

## Installation

Requirements:

* Python 3.10
* Poetry

Install the project:

* Install packages requirements with `poetry install`.
* Install pre-commit linters with `pre-commit install`.
