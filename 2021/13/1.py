#!/usr/bin/python3

import numpy as np

input = []
folds = []
dims = [0, 0]
with open('13/input.txt', 'r') as f:
    l = input
    for line in f.readlines():
        if line.count(',') > 0:
            l = list(map(int, line.strip().split(',')))
            for i in [0,1]:
                if l[i] > dims[i]:
                    dims[i] = l[i]
            input.append(l)
        elif line.count('=') > 0:
            l = line.strip().split('=')
            folds.append([l[0][-1], int(l[1])])
for i in [0,1]:
    dims[i] += 1

def printpaper(p):
    s = ''
    for i in range(len(p)):
        s += '\n'
        for j in range(len(p[0])):
            if p[i][j]:
                s += '#'
            else:
                s += '.'
    print(s)

def foldy(paper, fold):
    upper = paper[:][:fold]
    lower = paper[:][fold+1:]
    lower.reverse()
    new_paper = []
    for i in range(len(upper)):
        npl = []
        for j in range(len(upper[0])):
            npl.append(upper[i][j] or lower[i][j])
        new_paper.append(npl)
    return new_paper

def fold(paper, fold):
    if fold[0] == 'y':
        return foldy(paper, fold[1])
    else:
        p = np.array(paper).T.tolist()
        return np.array(foldy(p, fold[1])).T.tolist()

paper = [[False for x in range(dims[0])] for y in range(dims[1])]
for x, y in input:
    paper[y][x] = True

npl = paper
for f in folds:
    npl = fold(npl, f)

printpaper(npl)
