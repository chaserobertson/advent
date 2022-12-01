#!/usr/bin/python3

input = []
with open('2022/01/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

cals = []
cal = 0
for line in input:
    if line == '':
        cals.append(cal)
        cal = 0
    else:
        cal += int(line)

print(max(cals))
print(sum(list(reversed(sorted(cals)))[:3]))