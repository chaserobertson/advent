#!/usr/bin/python3

import numpy as np

input = []
with open('2022/08/input.txt', 'r') as f:
    input = f.read().splitlines()

heights = [[int(c) for c in line] for line in input]
visibilities = [[False for c in line] for line in input]

n, m = len(heights), len(heights[0])

# look down each row from left and right
for rownum in range(len(heights)):
    ranges = [range(0, n), range(n-1, -1, -1)]
    for rng in ranges:
        max_height = -1
        for colnum in rng:
            if max_height < heights[rownum][colnum]:
                visibilities[rownum][colnum] = True
                max_height = heights[rownum][colnum]

# look down each column from top and bottom
for colnum in range(len(heights[0])):
    ranges = [range(0, m), range(m-1, -1, -1)]
    for rng in ranges:
        max_height = -1
        for rownum in rng:
            if max_height < heights[rownum][colnum]:
                visibilities[rownum][colnum] = True
                max_height = heights[rownum][colnum]

print(sum([sum(vis) for vis in visibilities]))

# pt 2
def look_vert(rownum, colnum, up=0):
    rng = range(rownum-1, -1, -1) if up else range(rownum+1, n)
    height = heights[rownum, colnum]
    visible = 0
    for i in rng:
        visible += 1
        if heights[i, colnum] >= height:
            break
    return visible

def look_horiz(rownum, colnum, left=0):
    rng = range(colnum-1, -1, -1) if left else range(colnum+1, m)
    height = heights[rownum, colnum]
    visible = 0
    for i in rng:
        visible += 1
        if heights[rownum, i] >= height:
            break
    return visible

trees_visible = [[[0,0,0,0] for c in line] for line in input]

heights = np.array(heights)

# look down each row from left to right
for rownum in range(0, n):
    for colnum in range(0, m):
        trees_visible[rownum][colnum][0] = look_vert(rownum, colnum, 1)
        trees_visible[rownum][colnum][1] = look_horiz(rownum, colnum)
        trees_visible[rownum][colnum][2] = look_horiz(rownum, colnum, 1)
        trees_visible[rownum][colnum][3] = look_vert(rownum, colnum)

print(max([max([np.prod(v) for v in row]) for row in trees_visible]))
