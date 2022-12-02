#!/usr/bin/python3

scores = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3
}

results = {
    'lose': 0,
    'draw': 3,
    'win': 6
}

results2 = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

input = []
with open('2022/02/input.txt', 'r') as f:
    input = f.read().splitlines()

total = 0
total2 = 0
for game in input:
    p1, p2 = game.split(' ')
    total += scores[p2]
    diff = scores[p2] - scores[p1]
    if 0 < diff <= 1 or diff < -1:
        total += results['win']
    elif diff < 0 or diff > 1:
        total += results['lose']
    else:
        total += results['draw']

    total2 += results[results2[p2]]
    if results2[p2] == 'win':
        total2 += scores[p1] + 1 if scores[p1] + 1 <= 3 else 1
    elif results2[p2] == 'lose':
        total2 += scores[p1] - 1 if scores[p1] - 1 > 0 else 3
    else:
        total2 += scores[p1]

print(total)
print(total2)