#!/usr/bin/python3

import ast

input = []
with open('2022/13/test.txt', 'r') as f:
    input = [ast.literal_eval(x) for x in f.read().splitlines() if x]

def compare(left, right, depth=0, i=1):
    if not depth:
        print(f'== Pair {i} ==')
    print('  '*depth, '- Compare', left, 'vs', right)
    if type(left) == int and type(right) == int:
        return 2 if left < right else 1 if left == right else 0

    # listify integers if necessary
    left = [left] if type(left) == int else left
    right = [right] if type(right) == int else right

    for i in range(max(len(left), len(right))):
        if i >= len(right):
            print('  '*depth, 'Right side ran out of items')
            return 0
        elif i >= len(left):
            print('  '*depth, 'Left side ran out of items')
            return 2
        else:
            ordered = compare(left[i], right[i], depth=depth+2)
            if ordered != 1:
                side = 'Left' if ordered == 2 else 'Right'
                print('  '*depth, side+' is smaller')
                return ordered
            # pass here if ordered == 1 (both values equal)
    return 1 # no short-circuit so lists must be equal

ordered_pairs = [
    i//2+1 for i in range(0, len(input), 2) 
    if print() or compare(input[i], input[i+1], i=i//2+1)
]

print(ordered_pairs)
print(sum(ordered_pairs))
