#!/usr/bin/python3

import copy

input = []
with open('2022/05/input.txt', 'r') as f:
    input = f.read().splitlines()

stacks = [[] for i in range(0, len(input[0]), 4)]
procedure = []
for line in input:
    if '[' in line:
        for i, j in zip(range(len(stacks)), range(1, len(stacks)*4, 4)):
            if line[j] != ' ':
                stacks[i].append(line[j])
    elif 'move' in line:
        proc = line.split()
        procedure.append([int(x) for x in proc if x.isdigit()])

for stack in stacks:
    stack.reverse()

stacks2 = copy.deepcopy(stacks)

# v1 restacker
for proc in procedure:
    for i in range(proc[0]):
        temp = stacks[proc[1]-1].pop()
        stacks[proc[2]-1].append(temp)
print(''.join([s[-1] for s in stacks]))

#v2 restacker
stacks = stacks2
for proc in procedure:
    temp = stacks[proc[1]-1][-proc[0]:]
    stacks[proc[2]-1] = stacks[proc[2]-1] + temp
    stacks[proc[1]-1] = stacks[proc[1]-1][:-proc[0]]
print(''.join([s[-1] for s in stacks]))
