#!/usr/bin/python3

from ast import literal_eval
from functools import cmp_to_key

input = []
with open('2022/13/input.txt', 'r') as f:
    input = [literal_eval(x) for x in f.read().splitlines() if x]

pt2 = [[[2]], [[6]]]
input2 = input + pt2

def compare(left, right, depth=0, i=1):
    if not depth:
        print(f'== Pair {i} ==')
    print('  '*depth, '- Compare', left, 'vs', right)
    if type(left) == int and type(right) == int:
        return -1 if left < right else 0 if left == right else 1

    # listify integers if necessary
    left = [left] if type(left) == int else left
    right = [right] if type(right) == int else right

    for i in range(max(len(left), len(right))):
        if i >= len(right):
            print('  '*depth, 'Right side ran out of items')
            return 1
        elif i >= len(left):
            print('  '*depth, 'Left side ran out of items')
            return -1
        else:
            ordered = compare(left[i], right[i], depth=depth+2)
            if ordered != 0:
                side = 'Left' if ordered == -1 else 'Right'
                print('  '*depth, side+' is smaller')
                return ordered
            # pass here if ordered == 1 (both values equal)
    return 0 # no short-circuit so lists must be equal

ordered_pairs = [
    i//2+1 for i in range(0, len(input), 2) 
    if print() or compare(input[i], input[i+1], i=i//2+1) == -1
]

sorted_packets = sorted(input2, key=cmp_to_key(compare))
inds = [sorted_packets.index(p) for p in pt2]

print(sum(ordered_pairs))
print((inds[0] + 1) * (inds[1] + 1))
