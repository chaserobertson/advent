#!/usr/bin/python3

CRT_WIDTH = 40

input = []
with open('2022/10/input.txt', 'r') as f:
    input = f.read().splitlines()

instructions = [line.split() for line in input]
instructions.reverse()

signal_strengths = {c: 0 for c in range(20, 221, 40)}
op_stack = []

X = 1
x = []

cycle = 0
while instructions or op_stack:
    # record cycles of interest
    x.append(X)
    if cycle in signal_strengths:
        signal_strengths[cycle] = cycle * X
    cycle += 1

    # fiddly pt2 printing
    c = '#' if X-1 <= (cycle-2) % CRT_WIDTH <= X+1 else '.'
    print(c, end=f'\n' if not (cycle-1) % CRT_WIDTH else '')

    # execute pending operations if no delay
    if op_stack:
        delay -= 1
        if delay:
            continue
        X += op_stack.pop()

    # process new instruction
    instruction = instructions.pop()
    if len(instruction) > 1:
        op, val = instruction
        op_stack.append(int(val))
        delay = 2

print(sum(signal_strengths.values()))
