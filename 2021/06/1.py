#!/usr/bin/python3

input = []
with open('06/input.txt', 'r') as f:
    for line in f.readlines():
        for c in line.strip().split(','):
            input.append(int(c))

print(input)

fishes = input
num_days = 80
for day in range(0, num_days):
    new_fishes = []
    for j in range(0, len(fishes)):
        if fishes[j] == 0:
            fishes[j] = 6
            new_fishes.append(8)
        else:
            fishes[j] -= 1
    fishes += new_fishes

print(len(fishes))