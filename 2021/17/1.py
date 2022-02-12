#!/usr/bin/python3
from sys import maxsize

def range_extract(range_str):
    return [int(x) for x in range_str.strip()[2:].split('..')]    

input = ''
with open('17/input.txt', 'r') as f:
    for line in f.readlines():
        input = line.strip()
input = input.removeprefix('target area: ')

xstr, ystr = input.split(',')
xrange = range_extract(xstr)
yrange = range_extract(ystr)

maxy = -maxsize
hits = set()
for i in range(1, 1000):
    for j in range(-1000, 1000):
        position = [0, 0]
        velocity = [i, j]
        #print('initial', velocity)
        local_max = -maxsize
        for step in range(30):
            position[0] += velocity[0]
            position[1] += velocity[1]
            #print('position', position)
            if velocity[0] > 0:
                velocity[0] -= 1
            elif velocity[0] < 0:
                velocity[0] += 1
            velocity[1] -= 1
            #print('updated',velocity)

            if local_max < position[1]:
                local_max = position[1]

            if xrange[0] <= position[0] <= xrange[1]:
                if yrange[0] <= position[1] <= yrange[1]:
                    #print([i,j], 'hits at', position, 'w maxy', local_max)
                    hits.add((i,j))
                    print(len(hits))
                    if local_max > maxy:
                        maxy = local_max
                    break
            
print(maxy)
print(len(hits))