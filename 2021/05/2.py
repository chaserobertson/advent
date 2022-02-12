#!/usr/bin/python3
import numpy as np

input = []
with open('05/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

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
    
grid = [[0 for i in range(0, max_ind+1)] for i in range(0, max_ind+1)]
for coord in coords.copy():
    while coord[0] != coord[1]:
        # mark x1,y1
        grid[coord[0][0]][coord[0][1]] += 1
        # traverse x
        if coord[0][0] < coord[1][0]:
            coord[0][0] += 1
        elif coord[0][0] > coord[1][0]:
            coord[0][0] -= 1
        #traverse y
        if coord[0][1] < coord[1][1]:
            coord[0][1] += 1
        elif coord[0][1] > coord[1][1]:
            coord[0][1] -= 1
    grid[coord[0][0]][coord[0][1]] += 1

for row in np.array(grid).T.tolist():
    print(row)

overlaps = 0
for row in grid:
    for x in row:
        if x >= 2:
            overlaps += 1
print(overlaps)