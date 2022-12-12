#!/usr/bin/python3

from queue import PriorityQueue

class Node:
    def __init__(self, ind):
        self.ind = ind
        self.neighbors = set()
        self.dist = 9999999900
        self.visited = False
    def __str__(self):
        out = str(self.ind) + ' ' + str(self.dist)
        return out
    def __lt__(self, other):
        return self.dist < other.dist
    def distance(self, node):
        return abs(self.ind[0] - node.ind[0]) + abs(self.ind[1] - node.ind[1])


directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

input = []
with open('2022/12/input.txt', 'r') as f:
    input = f.read().splitlines()

n = len(input)
m = len(input[0])

start, end = None, None
nodes = {(i, j): Node((i,j)) for i in range(n) for j in range(m)}

for i, line in enumerate(input):
    for j, char in enumerate(line):
        if char == 'S':
            start = nodes[(i,j)]
            input[i] = input[i][:j] + chr(ord('a')) + input[i][j+1:]
        if char == 'E':
            end = nodes[(i,j)]
            input[i] = input[i][:j] + chr(ord('z')) + input[i][j+1:]

start, end = end, start

for i, line in enumerate(input):
    for j, char in enumerate(line):
        neighbors = []
        for dx, dy in directions:
            x, y = i + dx, j + dy
            if 0 <= x < n and 0 <= y < m:
                if ord(input[x][y]) - ord(input[i][j]) > -2:
                    nodes[(i,j)].neighbors.add(nodes[(x, y)])

start.dist = 0

queue = PriorityQueue()
queue.put(start)
while not queue.empty():
    current = queue.get()
    current.visited = True
    for ne in current.neighbors:
        dist = current.dist + 1
        if not ne.visited and dist < ne.dist:
            ne.dist = dist
            queue.put(ne)

print(end.dist)
