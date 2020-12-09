import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('', 'smol_input.txt')

with open(in_file) as input:
    lines = input.readlines()
