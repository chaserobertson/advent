#!/usr/bin/python3

LIMIT = 4000000
MOVES = [[1, 0], [-1, 0], [0, 1], [0, -1]]
TRAVS = [[-1, 1], [1, -1], [-1, -1], [1, 1]]
SEARCH_X = [0, LIMIT]
SEARCH_Y = [0, LIMIT]

class Sensor:
    def __init__(self, x, y, bx, by):
        self.x = x
        self.y = y
        self.bx = bx
        self.by = by
        self.r = self.dist(bx, by)
    def dist(self, x, y):
        return abs(self.x - x) + abs(self.y - y)
    def bdist(self, x, y):
        return abs(self.bx - x) + abs(self.by - y)
    def corners(self):
        return [[m[0]*self.r + self.x, 
                m[1]*self.r + self.y] 
                for m in MOVES]
    def detected(self, x, y):
        return int(self.dist(x, y) <= self.r)
    def traverse(self, sensors):
        corns = [[c[0]+m[0], c[1]+m[1]] for c, m in zip(self.corners(), MOVES)]
        for c, t in zip(corns, TRAVS):
            c = [t[0] + c[0], t[1] + c[1]]
            while c not in corns:
                errs = [s.detected(*c) for s in sensors]
                if sum(errs) == 0 and SEARCH_X[0] <= c[0] <= SEARCH_X[1] and SEARCH_Y[0] <= c[1] <= SEARCH_Y[1]:
                    return c
                c = [t[0] + c[0], t[1] + c[1]]
        return None

input = []
with open('2022/15/input.txt', 'r') as f:
    input = f.read().splitlines()

sensors = []
for line in input:
    s = line.split('=')
    x = int(s[1].split(',')[0])
    y = int(s[2].split(':')[0])
    by = int(s[-1])
    bx = int(s[-2].split(',')[0])
    sensors.append(Sensor(x, y, bx, by))

mat = {(i, j): '.' for i in range(-2, 26) for j in range(-2, 23)}
for i, sensor in enumerate(sensors):
    print(f'Traversing edges of sensor {i}')
    t = sensor.traverse(sensors)
    if t:
        print('Found signal at', t)
        print(t[0]*LIMIT + t[1]); break

# print(' '+''.join([f'{x:5}' for x in range(0, 26, 5)]))
# for j in range(-2, 23):
#     print(f'{j:2} ', end = '')
#     print(''.join([mat[i, j] for i in range(-2, 26)]))
