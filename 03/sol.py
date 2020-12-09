import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('03', 'input.txt')

TREE = '#'
# set x and y step size and direction
steps = [
    [1, 1],
    [3, 1],
    [5, 1],
    [7, 1],
    [1, 2]
]

with open(in_file) as input:
    lines = input.readlines()

# set max x and y coord
x_max, y_max = len(lines[0].strip()), len(lines)

mult = 1
# for each step option
for step in steps:
    x_step = step[0]
    y_step = step[1]
    # start having seen no trees (#), at first character
    trees, x, y = 0, 0, 0
    # until we reach the bottom of input
    while y < y_max:
        # add trees to seen
        if lines[y][x] == TREE:
            trees += 1
        # step to the next location, wrapping on x-axis
        x = (x + x_step) % x_max
        y += y_step

    mult *= trees
    print([step, trees, mult])
