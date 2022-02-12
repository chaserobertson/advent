#!/usr/bin/python3

import statistics

input = []
with open('07/input.txt', 'r') as f:
    for line in f.readlines():
        nums = line.strip().split(',')
        input = [int(n) for n in nums]

input.sort()

align = round(statistics.median(input))

spend = 0
for crab in input:
    spend += abs(crab - align)

print(spend)

spends = [0 for x in range(min(input), max(input)+1)]
for i in range(0, len(spends)):
    for crab in input:
        spends[i] += abs(crab - i)

print(min(spends))