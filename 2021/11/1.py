#!/usr/bin/python3

flashes = [0]
octopi = []
with open('11/input.txt', 'r') as f:
    for line in f.readlines():
        row = []
        for r in line.strip():
            row.append(int(r))
        octopi.append(row)
m = len(octopi)
n = len(octopi[0])

def printer():
    for row in octopi:
        s = ''
        for c in row:
            s += str(c)
        print(s)
    print()

def flashed(i, j):
    if octopi[i][j] == 0:
        return
    else:
        octopi[i][j] += 1
        if octopi[i][j] > 9:
            flash(i, j)

def flash(i, j):
    flashes[0] += 1
    octopi[i][j] = 0
    if i > 0:
        flashed(i-1, j)
        if j > 0:
            flashed(i-1, j-1)
        if j < n-1:
            flashed(i-1, j+1)
    if i < m-1:
        flashed(i+1, j)
        if j > 0:
            flashed(i+1, j-1)
        if j < n-1:
            flashed(i+1, j+1)
    if j > 0:
        flashed(i, j-1)
    if j < n-1:
        flashed(i, j+1)

print('Before any steps:')
printer()

steps = 100
for step in range(1, steps+1):
    for i in range(0, m):
        for j in range(0, n):
            octopi[i][j] += 1
    
    for i in range(0, m):
        for j in range(0, n):
            if octopi[i][j] > 9:
                flash(i, j)

    print('After step 1:')
    printer()
print(flashes)