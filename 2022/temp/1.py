#!/usr/bin/python3

input = []
with open('2022/0/test.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

print(input)
