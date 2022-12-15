#!/usr/bin/python3

ROW = 2000000

def sweep(x, y, r, b, row=None):
    rng = range(-r, r + 1)
    grid = set()
    for i in rng:
        for j in [row-y]:
            # limit by nearest beacon radius
            if abs(i) + abs(j) <= r:
                point = (x + i, y + j)
                # limit by specified row if pt1
                if point not in b and (row == None or y + j == row):
                    grid.add(point)
    return grid

input = []
with open('2022/15/input.txt', 'r') as f:
    input = f.read().splitlines()

sensors = []
beacons = set()
blocked_row = set()
for line in input:
    s = line.split('=')
    x = int(s[1].split(',')[0])
    y = int(s[2].split(':')[0])
    by = int(s[-1])
    bx = int(s[-2].split(',')[0])
    beacons.add((bx, by))
    radius = abs(x - bx) + abs(y - by)
    s_blocked = sweep(x, y, radius, beacons, ROW)
    blocked_row.update(s_blocked)

print(len(blocked_row))
