#!/usr/bin/python3

import math
from typing import no_type_check

originals = []
bin_len = 0
with open('03/input.txt', 'r') as f:
    for line in f.readlines():
        in_line = line.strip()
        originals.append(in_line)
        bin_len = len(in_line)

def get_rating(indices, depth, mirror):
    if len(indices) <= 1 or depth >= bin_len:
        return originals[indices[0]]

    positional = 0
    num_inputs = 0
    for index in indices:
        input = originals[index]
        num_inputs += 1
        if input[depth] == '1':
                positional += 1
    proportion = positional / num_inputs
    if proportion == 0.5:
        common = 1 ^ mirror
    else:
        common = round(proportion) ^ mirror
    print(depth, num_inputs, positional, common)

    new_indices = []
    for index in indices:
        if originals[index][depth] == str(common):
            new_indices.append(index)

    print(new_indices)
    return get_rating(new_indices, depth+1, mirror)

oxy_indices = [i for i in range(0, len(originals))]
scrub_indices = oxy_indices.copy()

oxy_rating = get_rating(oxy_indices, 0, 0)
scrub_rating = get_rating(scrub_indices, 0, 1)

binaries = [oxy_rating, scrub_rating]
decimals = [0, 0]
for i in range(0, len(binaries)):
    for digit in binaries[i]:
        decimals[i] = (decimals[i] << 1) | int(digit)

print(math.prod(decimals))