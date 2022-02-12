#!/usr/bin/python3
from math import prod

class Tile():
    def __init__(self, strlist):
        self.id = strlist[0].split()[1][0:4]
        self.tile = strlist[1:]
        left, right = '', ''
        for s in strlist[1:]:
            left += s[0]
            right += s[-1]
        self.borders = [strlist[1], strlist[-1], left, right]
        self.magnitudes = [s.count('#') for s in self.borders]
        #self.matches = {}

    def __str__(self):
        out = 'Tile '+self.id+':'
        for border in self.borders:
            out += '\n'+border
        return out

input = []
with open('advent2020/20/input.txt', 'r') as f:
    raw_tile = []
    for line in f.readlines():
        if line == '\n':
            input.append(raw_tile)
            raw_tile = []
        else:
            raw_tile.append(line.strip())

# for each tile, for remaining tiles
# check borders and add to general match set, per border set
tiles = [Tile(t) for t in input]
tilemap = {t.id: t for t in tiles}
matches = {}
for i in range(len(tiles)):
    for j in range(i, len(tiles)):
        if i == j:
            continue
        for x in range(len(tiles[i].borders)):
            b1 = tiles[i].borders[x]
            for y in range(len(tiles[j].borders)):
                b2 = tiles[j].borders[y]
                if b1 == b2 or b1 == b2[::-1]:
                    matches.setdefault(tiles[i].id, set())
                    matches.setdefault(tiles[j].id, set())
                    matches[tiles[i].id].add(tiles[j].id)
                    matches[tiles[j].id].add(tiles[i].id)
                    #tiles[i].matches.setdefault(tiles[j].id, [])
                    #tiles[i].matches[tiles[j].id].append(y)
                    #tiles[j].matches.setdefault(tiles[i].id, [])
                    #tiles[j].matches[tiles[i].id].append(x)

corners = set()
for k,v in matches.items():
    if len(v) == 2:
        corners.add(k)

# for each tile, if len match set <= 2, is corner
print(prod([int(c) for c in corners]))