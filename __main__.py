"""
SIMPLE AF ADVENT OF CODE LAUNCHER

Simple way to run code without retyping a complicated command for each day.

Usage: python . YEAR DAY USE_EXAMPLE_FILE?
"""
import subprocess
import sys
import os

# https://stackoverflow.com/a/715455
YES_STRINGS = ['true', '1', 't', 'y', 'yes', 'yeah', 'yup', 'certainly', 'uh-huh']

try:
    year = sys.argv[1]
    day = sys.argv[2]
    try:
        example = sys.argv[3].lower() in YES_STRINGS
    except:
        example = False

    current_python = os.path.join(os.path.dirname(sys.executable), "python")
    working_dir = os.path.dirname(os.path.realpath(__file__))

    path = os.path.join(working_dir, year, f"day{day}")

    # check if i want to test with examples from aoc
    if example:
        text_file = "examples.txt"
    else:
        text_file = "input.txt"

    # python 2015/day2 2015/day2/input.txt
    subprocess.run([f"{current_python}", path, os.path.join(path, text_file)])  # , shell=True) # causes python to run in interactive mode...
except:
    print(__doc__)