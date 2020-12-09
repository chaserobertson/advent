import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('03', 'smol_input.txt')

with open(in_file) as input:
    lines = input.readlines()
