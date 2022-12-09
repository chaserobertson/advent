#!/usr/bin/python3

import numpy as np

NUM_KNOTS = 10
GRID_SIZE = 16
MOVES = {
    'R': [1, 0],
    'L': [-1, 0],
    'U': [0, 1],
    'D': [0, -1]
}

# for debugging
def print_grid(knots, n=GRID_SIZE):
    knot_list = [list(knot) for knot in knots]
    for i in range(n-1,-6,-1):
        for j in range(-11, n):
            c = '.'
            if [j, i] in knot_list:
                c = knot_list.index([j, i])
            print(c, end='')
        print()
    print()


input = []
with open('2022/09/input.txt', 'r') as f:
    input = f.read().splitlines()

tail_positions = set()
knots = np.zeros(shape=(NUM_KNOTS, 2), dtype=int)

for line in input:
    direction, distance = line.split()
    distance = int(distance)

    for i in range(distance):
        knots[0] += MOVES[direction]

        for i in range(1, len(knots)):
            dist = knots[i-1] - knots[i]
            abs_dist = np.abs(dist)
            step = np.sign(dist)

            if sum(abs_dist) > 2:
                # diagonal - take 1 step in both directions
                knots[i] += step
            else:
                # take 1 step in direction of gap
                knots[i] += step * (abs_dist > 1)

        tail_positions.add(tuple(knots[-1])) 
    #print_grid(knots)

print(len(tail_positions))
