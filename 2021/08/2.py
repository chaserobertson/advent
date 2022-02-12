#!/usr/bin/python3

ZERO = 'abcefg'
ONE = 'cf'
TWO = 'acdeg'
THREE = 'acdfg'
FOUR = 'bcdf'
FIVE = 'abdfg'
SIX = 'abdefg'
SEVEN = 'acf'
EIGHT = 'abcdefg'
NINE = 'abcdfg'
ALL = {x: [y for y in EIGHT] for x in EIGHT}
ops = ['in', 'out']

patterns = []
with open('08/input.txt', 'r') as f:
    for line in f.readlines():
        input = line.split('|')
        i = input[0].strip().split()
        o = input[1].strip().split()
        pattern = dict()
        for i in range(0, len(ops)):
            sorted = []
            for x in input[i].strip().split():
                s = []
                for y in x:
                    s.append(y)
                #s.sort()
                sorted.append(''.join(s))
            pattern.setdefault(ops[i], sorted)
        patterns.append(pattern)

sum = 0
for pattern in patterns:
    in_pat = pattern['in']
    out_pat = pattern['out']
    digits = {x: '' for x in range(0, 10)}
    letters = {x: set(EIGHT) for x in EIGHT}
    pat_remaining = in_pat.copy()
    for i in in_pat:
        l = len(i)
        if l == 2:
            digits[1] = i
            letters.setdefault(ONE, set(i))
            pat_remaining.remove(i)
        elif l == 3:
            digits[7] = i
            letters.setdefault(SEVEN, set(i))
            pat_remaining.remove(i)
        elif l == 4:
            digits[4] = i
            letters.setdefault(FOUR, set(i))
            pat_remaining.remove(i)
        elif l == 7:
            digits[8] = i
            letters.setdefault(EIGHT, set(i))
            pat_remaining.remove(i)

    letters['a'] = set(digits[7]).difference(digits[1])
    letters.setdefault('bd', set(digits[4]).difference(digits[1]))
    a1bd = letters['a'].union(set(digits[1]), letters['bd'])
    letters.setdefault('eg', set(digits[8]).difference(a1bd))
    abdeg = letters['a'].union(letters['bd'], letters['eg'])
    for i in pat_remaining:
        if abdeg.issubset(i):
            digits[6] = i
    pat_remaining.remove(digits[6])

    letters['f'] = set(digits[6]).difference(abdeg)
    letters['c'] = set(digits[1]).difference(letters['f'])
    for i in pat_remaining:
        if not letters['f'].issubset(i):
            digits[2] = i
    pat_remaining.remove(digits[2])

    aceg = letters['a'].union(letters['c'], letters['eg'])
    letters['d'] = set(digits[2]).difference(aceg)
    letters['b'] = letters['bd'].difference(letters['d'])
    zero_set = set(digits[8]).difference(letters['d'])
    for i in pat_remaining:
        if zero_set == set(i):
            digits[0] = i
    pat_remaining.remove(digits[0])

    for i in pat_remaining:
        if len(i) == 6:
            digits[9] = i
    pat_remaining.remove(digits[9])
    
    letters['e'] = set(digits[8]).difference(set(digits[9]))
    letters['g'] = letters['eg'].difference(letters['e'])
    for i in pat_remaining:
        if letters['b'].issubset(i):
            digits[5] = i
        else:
            digits[3] = i

    output = []
    for out in out_pat:
        for k, v in digits.items():
            if set(v) == set(out):
                output.append(str(k))
    value = int(''.join(output))
    sum += value
print(sum)

# 1 = cf
# 4 = bcdf
# 7 = acf
# 8 = abcdefg
# a = 7.remove(1)
# bd = 4.remove(1)
# eg = 8.remove(a, 1, bd)
# 6 is only digit with abdeg
# f = 6.remove(abdeg)
# c = 1.remove(f)
# 2 is only digit without f
# d = 2.remove(a, c, eg)
# b = bd.remove(d)
# 0 = 8.remove(d)
# 9 is only remaining len(6)
# e = 8.remove(9)
# g = eg.remove(e)
# 3 = 8.remove(b, e)
# 5 = 6.remove(e)

# a does not appear in 1, 4
# b does not appear in 1, 2, 3, 7
# c does not appear in 5, 6
# d does not appear in 0, 1, 7
# e does not appear in 1, 3, 4, 5, 7, 9
# f does not appear in 2
# g does not appear in 1, 4, 7
