#!/usr/bin/python3

import math

input = []
with open('09/input.txt', 'r') as f:
    for line in f.readlines():
        row = [int(x) for x in line.strip()]
        input.append(row)

low_points = []

for j in range(0, len(input)):
    row = input[j]
    for i in range(0, len(row)):
        isLow = True
        if i > 0:
            isLow &= input[j][i] < input[j][i-1]
        if i < len(row) - 1:
            isLow &= input[j][i] < input[j][i+1]
        if j > 0:
            isLow &= input[j][i] < input[j-1][i]
        if j < len(input) - 1:
            isLow &= input[j][i] < input[j+1][i]
        if isLow:
            low_points.append([j, i])

seen = [[False 
for x in range(0, len(input[0]))]
for y in range(0, len(input))]

def higher_neighbors(j, i):
    if seen[j][i] or input[j][i] == 9:
        return 0
    
    high_neighbors = 1
    seen[j][i] = True
    if i > 0:
        high_neighbors += higher_neighbors(j, i-1)
    if i < len(row) - 1:
        high_neighbors += higher_neighbors(j, i+1)
    if j > 0:
        high_neighbors += higher_neighbors(j-1, i)
    if j < len(input) - 1:
        high_neighbors += higher_neighbors(j+1, i)
    return high_neighbors

sizes = []
for coords in low_points:
    sizes.append(higher_neighbors(coords[0], coords[1]))

sizes.sort()
print(math.prod(sizes[-3:]))