#!/usr/bin/python3

input = []
with open('2022/04/input.txt', 'r') as f:
    input = f.read().splitlines()

contains = 0
overlaps = 0

for line in input:
    ranges = line.split(",")
    edges = ranges[0].split('-') + ranges[1].split('-')
    edges = [int(x) for x in edges]

    if edges[0] >= edges[2] and edges[1] <= edges[3] \
        or edges[0] <= edges[2] and edges[1] >= edges[3]:
        contains += 1

    if edges[2] <= edges[0] <= edges[3] \
        or edges[2] <= edges[1] <= edges[3] \
        or edges[0] <= edges[2] <= edges[1] \
        or edges[0] <= edges[3] <= edges[1]:
        overlaps += 1

print(contains)
print(overlaps)