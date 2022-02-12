#!/usr/bin/python3

import sys
from typing import OrderedDict

risks = []
with open('15/input.txt', 'r') as f:
    for line in f.readlines():
        row = []
        for c in line.strip():
            row.append(int(c))
        risks.append(row)

m = len(risks)
n = len(risks[0])

risksums = [[sys.maxsize for x in range(n)] for y in range(m)]
risksums[0][0] = 0

visited = set()
not_visited = {(0,0)}

while len(not_visited) > 0:
    x, y = not_visited.pop()

    neighbors = set()
    if x > 0:
        neighbors.add((x-1, y))
    if x < m-1:
        neighbors.add((x+1, y))
    if y > 0:
        neighbors.add((x, y-1))
    if y < n-1:
        neighbors.add((x, y+1))

    for i, j in neighbors:
        if risksums[i][j] > risksums[x][y] + risks[i][j]:
            risksums[i][j] = risksums[x][y] + risks[i][j]
            not_visited.add((i, j))
    visited.add((x, y))

for row in risksums:
    print(row)
print(risksums[-1][-1])