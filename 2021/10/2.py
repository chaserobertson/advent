#!/usr/bin/python3

magic_multiple = 5
points = {
    ')': 1, 
    ']': 2, 
    '}': 3, 
    '>': 4
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
fixers = []
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
        if i == len(line) -1 and len(stack) != 0:
            fixers.append(stack)

scores = []
for f in fixers:
    f.reverse()
    score = 0
    for c in f:
        score *= magic_multiple
        score += points[match[c]]
    scores.append(score)
scores.sort()
print(scores[len(scores) // 2])