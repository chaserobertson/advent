#!usr/bin/python3

with open('01/input.txt', 'r') as file:
    sums = []
    increases = 0

    left = int(file.readline())
    center = int(file.readline())
    right = int(file.readline())
    for next in file.readlines():
        sum = left + center + right
        delta = int(next) - left
        if delta > 0:
            increases += 1
        left = center
        center = right
        right = int(next)

print(increases)