#!/usr/bin/python3

input = []
with open('2022/06/input.txt', 'r') as f:
    input = f.read().splitlines()

def first_distinct_set(lines, set_len):
    for line in lines:
        for i in range(set_len, len(line)):
            if len(set(line[i-set_len:i])) == set_len:
                print(i)
                break

first_distinct_set(input, 4)
first_distinct_set(input, 14)