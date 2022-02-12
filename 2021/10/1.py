#!/usr/bin/python3

points = {
    ')': 3, 
    ']': 57, 
    '}': 1197, 
    '>': 25137
}

match = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

input = []
with open('10/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

losers = []
for line in input:
    stack = []
    for i in range(0, len(line)):
        c = line[i]
        if c in match.keys():
            stack.append(c)
        elif c == match[stack[-1]]:
            stack.pop()
        else:
            if i != len(line) - 1:
                losers.append(c)
                break

sum = 0
for loser in losers:
    sum += points[loser]
print(sum)