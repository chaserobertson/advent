#!/usr/bin/python3

import math, statistics

input = []
with open('07/input.txt', 'r') as f:
    for line in f.readlines():
        nums = line.strip().split(',')
        input = [int(n) for n in nums]

align = math.floor(statistics.mean(input))

total_spend = 0
for crab in input:
    dist = abs(crab - align)
    if dist % 2 == 0:
        spend = (dist + 1) * (dist // 2)
    else:
        spend = dist + (dist * (dist // 2))
    total_spend += spend

print(align)
print(total_spend)
