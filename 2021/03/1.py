#!/usr/bin/python3

import math

with open('03/input.txt', 'r') as f:
    positionals = []
    num_lines = 0

    for line in f.readlines():
        if positionals == []:
            positionals = [0 for i in range(0, len(line) - 1)]
        num_lines += 1
        for i in range(0, len(line)):
            if line[i] == '1':
                positionals[i] += 1
    
    print(num_lines, positionals)
    gamma = [round(x / num_lines) for x in positionals]
    print(gamma)
    epsilon = [round((num_lines - x) / num_lines) for x in positionals]
    print(epsilon)

    binaries = [gamma, epsilon]
    decimals = [0, 0]
    for i in range(0, len(binaries)):
        for digits in binaries[i]:
            decimals[i] = (decimals[i] << 1) | digits

    print(math.prod(decimals))
