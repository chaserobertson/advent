#!/usr/bin/python3

START = [0, 500]
pt2 = 0 # 170 for full pt2 answer

input = []
with open('2022/14/input.txt', 'r') as f:
    input = f.read().splitlines()

# get all x and y values and list of coordinates in each path
xs, ys, paths = [], [], []
for line in input:
    coords = line.split(' -> ')
    path = []
    for c in coords:
        y, x = [int(c_) for c_ in c.split(',')]
        ys.append(y)
        xs.append(x)
        path.append([x, y])
    paths.append(path)

# add new path on bottom of matrix for pt2
if pt2:
    lim_y = min(ys) - pt2, max(ys) + pt2
    new_x = [max(xs) + 2 for i in range(2)]
    xs += new_x
    ys += lim_y
    paths.append([[new_x[i], lim_y[i]] for i in range(2)])

# adjust y values so min y is 0
orig_min_y = min(ys)
for i in range(len(ys)):
    ys[i] -= orig_min_y
for i in range(len(paths)):
    for j in range(len(paths[i])):
        paths[i][j][1] -= orig_min_y

# make character matrix
n, m = max(xs) + 1, max(ys) + 1
if pt2:
    mat = [['.' if x < n-1 else '#' for y in range(m)] for x in range(n)]
else:
    mat = [['.' for y in range(m)] for x in range(n)]

def print_mat(mat):
    yrng = range(m)
    print('   '+' '.join([f'{y:2}' for y in yrng]))
    for i in range(START[0], n):
        print(f'{i:3} '+' '.join([f'{x:2}' for x in mat[i]]))

# creates a coordinate path from two endpoints that share x or y
def rng(c1, c2):
    delta = [c2_ - c1_ for c1_, c2_ in zip(c1, c2)]
    pos = delta[0] >= 0 and delta[1] >= 0
    ind = abs(delta[0]) < abs(delta[1])
    scale = max([abs(x) for x in delta]) + 1
    r = [[c1[not ind], c1[not ind]] for i in range(scale)]
    for i in range(len(r)):
        r[i][ind] = c1[ind] + i * (1 if pos else -1)
    return r

# fill matrix with paths between each pair of coordinates
for path in paths:
    c1 = path[0]
    for c2 in path[1:]:
        for x, y in rng(c1, c2):
            mat[x][y] = '#'
        c1 = c2

# sand particles falling until stopped at source or reach matrix edge
sand = 0
stopped = False
while not stopped:
    sx, sy = START[0], START[1] - orig_min_y
    falling = True
    while falling:
        dx_in = (sx + 1) < n
        if dx_in and mat[sx+1][sy] == '.':
            sx += 1
        elif dx_in and sy-1 >= 0 and mat[sx+1][sy-1] == '.': 
            sx += 1; sy -= 1
        elif dx_in and sy+1 < m and mat[sx+1][sy+1] == '.':
            sx += 1; sy += 1
        else:
            falling = False
            if pt2 or dx_in and sy-1 >= 0 and sy+1 < m:
                mat[sx][sy] = 'o'
            else:
                stopped = True  
    if sx == START[0] and sy == START[1] - orig_min_y:
        # sand remains at start - should only happen at end of pt2
        stopped = True
    sand += 1

if pt2:
    print(sand)
else:
    print_mat(mat)
    print(sand - 1)
