#!/usr/bin/python3

import numpy as np
from queue import PriorityQueue

def chars_to_ints(chars):
    return [ord(char) - ord('a') for char in chars]

def to_tup(arr):
    return tuple([x[0] for x in arr])

def grid_neighbors(shape, current):
    n = np.array(current) + np.array([[1,0], [-1,0], [0,1], [0,-1]])
    valid = np.where(np.all(n >= 0, axis=1) & np.all(n < shape, axis=1))
    return [tuple(x) for x in n[valid]]

def valid_neighbors(grid, current):
    neighbors = grid_neighbors(grid.shape, current)
    return [x for x in neighbors if grid[x] - grid[current] >= -1]

input = []
with open('2022/12/input.txt', 'r') as f:
    input = np.array([chars_to_ints(l) for l in f.read().splitlines()])

start = to_tup(np.where(input == chars_to_ints('S')))
end = to_tup(np.where(input == chars_to_ints('E')))

input[start] = 0
input[end] = max([input[x] for x in grid_neighbors(input.shape, end)])

start, end = end, start

paths = np.ones(input.shape) * np.inf
paths[start] = 0

visited = np.zeros(input.shape)
pq = PriorityQueue()
pq.put((0, start))

while not pq.empty():
    d, current = pq.get()
    for neighbor in valid_neighbors(input, current):
        path = paths[current] + 1
        if not visited[neighbor] and path < paths[neighbor]:
            paths[neighbor] = paths[current] + 1
            pq.put((path, neighbor))
    visited[current] += 1

print(paths[end])
print(np.min(paths[np.where(input == 0)]))
