#!/usr/bin/python3
import numpy as np

input = []
with open('05/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

print(input)

max_ind = 0
coords = []
for line in input:
    coord = []
    origin, fin = line.split(' -> ')
    origin = origin.split(',')
    fin = fin.split(',')
    coord.append([int(origin[0]), int(origin[1])])
    coord.append([int(fin[0]), int(fin[1])])
    coords.append(coord)
    for x in [c for coo in coord for c in coo]:
        if int(x) > max_ind:
            max_ind = int(x)

print(coords)
    
grid = [[0 for i in range(0, max_ind+1)] for i in range(0, max_ind+1)]
for coord in coords.copy():
    # if only x differs e.g. horizontal
    if coord[0][0] != coord[1][0] and coord[0][1] == coord[1][1]:
        print('horizontal '+str(coord))
        while coord[0][0] < coord[1][0]:
            grid[coord[0][0]][coord[0][1]] += 1
            coord[0][0] += 1
        while coord[0][0] > coord[1][0]:
            grid[coord[0][0]][coord[0][1]] += 1
            coord[0][0] -= 1
        grid[coord[0][0]][coord[0][1]] += 1
    # if only y differs e.g. vertical
    elif coord[0][1] != coord[1][1] and coord[0][0] == coord[1][0]:
        print('vertical '+str(coord))
        while coord[0][1] < coord[1][1]:
            grid[coord[0][0]][coord[0][1]] += 1
            coord[0][1] += 1
        while coord[0][1] > coord[1][1]:
            grid[coord[0][0]][coord[0][1]] += 1
            coord[0][1] -= 1
        grid[coord[0][0]][coord[0][1]] += 1
    else:
        print('skipped ' + str(coord))

for row in np.array(grid).T.tolist():
    print(row)

overlaps = 0
for row in grid:
    for x in row:
        if x >= 2:
            overlaps += 1
print(overlaps)