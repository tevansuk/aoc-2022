import importlib
import os
import subprocess
import sys
from pathlib import Path

from num2words import num2words


def main():
    if len(sys.argv) != 2:
        print("Usage: poetry day [N]")
        sys.exit(-1)
    day = int(sys.argv[1])
    print(f"Yo its day {day}")
    dayw = num2words(day).replace("-", "_")
    module_name = f"aoc.{dayw}"
    input_file = Path(__file__).parent.parent / "resources" / f"{dayw}.txt"
    try:
        mod = importlib.import_module(module_name)
        func = getattr(mod, "main")
    except (ModuleNotFoundError, AttributeError):
        print(f"No such module/function {module_name}.main")
        sys.exit(-1)
    print(f"Running {module_name}.main")
    sys.exit(func(input_file))


def make_my_day():
    if len(sys.argv) != 2:
        print("Usage: poetry mkday [N]")
        sys.exit(-1)
    dayw = num2words(int(sys.argv[1])).replace("-", "_")
    root = Path(__file__).parent.parent
    pyfile = root / "aoc" / f"{dayw}.py"
    if not pyfile.exists():
        pyfile.write_text(
            """from dataclasses import dataclass
from pathlib import Path


def main(datafile: Path):
    data = parse_data(datafile)
    print(f"Q1: {{data}}")
    print(f"Q2: {{data}}")


def parse_data(datafile: Path):
    with datafile.open() as fp:
        return [line for line in fp.readlines()]
"""
        )
    testfile = root / "tests" / f"test_{dayw}.py"
    if not testfile.exists():
        testfile.write_text(
            f"""from pathlib import Path

import pytest

from aoc.{dayw} import *


@pytest.fixture
def data():
    return parse_data(Path(__file__).parent / "{dayw}.txt")


def test_parse_data(data):
    assert len(data) == 0
"""
        )
    testdata = root / "tests" / f"{dayw}.txt"
    if not testdata.exists():
        testdata.write_text("")
    files = [pyfile, testfile, testdata]
    if os.environ.get("EDITOR") == "vim":
        subprocess.check_call(["vim", "-o", *files])
    else:
        print("Created the following files:", *files, sep="\n")
