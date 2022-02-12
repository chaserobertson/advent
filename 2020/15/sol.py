import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('15', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

FIN = 30000000

starting_numbers = lines[0].strip().split(',')
numbers = [int(num) for num in starting_numbers]
print('Starting numbers: ' + str(numbers))

turns = {}
for i in range(0, len(numbers)):
    turns[numbers[i]] = [i+1]

start = len(numbers) + 1
for turn in range(start, FIN + 1):
    last_spoken = numbers[-1]
    turns_spoken = turns.setdefault(last_spoken, [])
    if len(turns_spoken) > 1:
        next_digit = turns_spoken[-1] - turns_spoken[-2]
        numbers.append(next_digit)
        digit_turns = turns.setdefault(next_digit, [])
        digit_turns.append(turn)
    else:
        numbers.append(0)
        digit = turns.setdefault(0, [])
        digit.append(turn)

print('The ' + str(FIN) + 'th number is: ' + str(numbers[-1]))
