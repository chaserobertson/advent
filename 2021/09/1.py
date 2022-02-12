#!/usr/bin/python3

input = []
with open('09/input.txt', 'r') as f:
    for line in f.readlines():
        row = [int(x) for x in line.strip()]
        input.append(row)

risk_levels = []
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
        low_points[j][i] = isLow
        if isLow:
            risk_levels.append(input[j][i] + 1)

print(sum(risk_levels))