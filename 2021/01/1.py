#!usr/bin/python3

with open('01/input.txt', 'r') as file:
    increases = 0

    previous = file.readline()
    for line in file.readlines():
        delta = int(line) - int(previous)
        if delta > 0:
            increases += 1
        previous = line

print(increases)