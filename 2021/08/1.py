#!/usr/bin/python3

patterns = []
with open('08/input.txt', 'r') as f:
    for line in f.readlines():
        input = line.split('|')
        patterns.append({'in': input[0].strip().split(),
        'out': input[1].strip().split()})

# for pattern in patterns:
#    print('IN', pattern['in'], '\n', 'OUT', pattern['out'])

unique_digits = 0
for pattern in patterns:
    for val in pattern['out']:
        if len(val) in {2, 3, 4, 7}:
            unique_digits += 1

print(unique_digits)