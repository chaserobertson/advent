#!/usr/bin/python3

import ast
import numpy as np
from itertools import zip_longest

input = []
with open('2022/13/test.txt', 'r') as f:
    input = [ast.literal_eval(x) for x in f.read().splitlines() if x]

#input += [[[2]], [[6]]]

def zipify(lst):
    out = []
    cols = [0]
    for z in zip_longest(*lst, fillvalue=0):
        cols[0] += 1
        types = [type(x) for x in z]
        typeset = set(types)
        if len(typeset) > 1:
            zl = [[x] if type(x) != list else [0] if x == [] else x for x in z]
            out_, len_ = zipify(zl)
            out += out_
            cols += len_
        else:
            out.append(z)
            cols.append(len(z))
        print(cols)
    return out, cols

zipped, lens = zipify(input)
mat = np.transpose(np.array(zipped))
print(mat)
order = np.argsort(mat, axis=0)

print(order)
print(lens)

for i in order:
    print(input[i])
