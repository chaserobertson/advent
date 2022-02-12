#!/usr/bin/python3

input = []
with open('12/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

def traverse(connections, p):
    x = p[-1]
    if x == 'end':
        return [p]
    
    paths = []
    for n in connections[x]:
        lowers = [z for z in p if z.islower()]
        lowerset = set(lowers)
        lowertwice = len(lowers) - len(lowerset) < 1
        if n.isupper() or (n not in p or lowertwice):
            paths += traverse(connections, p + [n])
    return paths

connections = {}
for line in input:
    origin, dest = line.split('-')
    connections.setdefault(origin, [])
    connections.setdefault(dest, [])
    if origin != 'end' and dest != 'start':
        connections[origin].append(dest)
    if origin != 'start' and dest != 'exit':
        connections[dest].append(origin)

paths = traverse(connections, ['start'])
for p in paths:
    print(p)
print(len(paths))