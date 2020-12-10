import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('06', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

groups = []
group = []
for line in lines:
    if line == '\n':
        if group != []:
            groups.append(group)
            group = []
    else:
        group.append(line.strip())
if group != []:
    groups.append(group)

print('part 1')
counts = []
for group in groups:
    group_set = ''
    for individual in group:
        group_set += individual
    counts.append(len(set(group_set)))

print(sum(counts))

print('part 2')
counts = []
for group in groups:
    group_set = {}
    for individual in group:
        for ch in individual:
            item = group_set.setdefault(ch, 0)
            group_set[ch] += 1
    # print(group_set)

    all_yes = 0
    l = len(group)
    for item in group_set.values():
        if item == l:
            all_yes += 1
    counts.append(all_yes)

# print(counts)
print(sum(counts))
