#!/usr/bin/python3

import string

letters = string.ascii_lowercase + string.ascii_uppercase
priority = {l: i+1 for i, l in enumerate(letters)}

input = []
with open('2022/03/input.txt', 'r') as f:
    input = f.read().splitlines()

z = ord('a') - 1

commons = []
for bag in input:
    mid = len(bag) // 2
    common = set(bag[:mid]).intersection(bag[mid:])
    commons += list(common)

print(sum([priority[x] for x in commons]))

badges = []
for i in range(0, len(input), 3):
    b = set(input[i]).intersection(input[i+1]).intersection(input[i+2])
    badges += list(b)
    
print(sum([priority[x] for x in badges]))