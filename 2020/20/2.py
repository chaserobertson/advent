#!/usr/bin/python3
from math import prod, sqrt
import numpy as np

MON_STR = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''
monster = [[c for c in l] for l in MON_STR.split('\n')]

class Tile():
    def __init__(self, id, strlist):
        self.id = id
        left, right = '', ''
        self.tile = []
        line = []
        for s in strlist:
            left += s[0]
            right += s[-1]
            for c in s:
                line.append(c)
            self.tile.append(line)
            line = []
        self.borders = [
            strlist[0], 
            right, 
            strlist[-1][::-1], 
            left[::-1]
            ]
        self.magnitudes = [s.count('#') for s in self.borders]
        #self.matches = {}

    def __str__(self):
        out = 'Tile '+self.id+':'
        for s in self.tile:
            out += '\n'
            for c in s:
                out += c
        return out

    def rotate(self):
        self.tile = list(zip(*self.tile[::-1]))
        self.borders = self.borders[1:] + [self.borders[0]]

    def flipx(self):
        self.tile = [reversed(l) for l in self.tile]
        for i in [0, 2]:
            self.borders[i] = self.borders[i][::-1] 
        temp = self.borders[1]
        self.borders[1] = self.borders[3]
        self.borders[3] = temp

    def flipy(self):
        self.tile = self.tile[::-1]
        for i in [1, 3]:
            self.borders[i] = self.borders[i][::-1] 
        temp = self.borders[0]
        self.borders[0] = self.borders[2]
        self.borders[2] = temp

    def trymatch(self, other, border):
        o_border = other.borders[(border + 2) % 4]
        if self.borders[border] == o_border:
            return True
        for z in [self.flipx, self.flipy]:
            for i in range(3):
                print(self.borders[border], o_border)
                self.rotate()
                if self.borders[border] == o_border:
                    return True
            z()
        return False

tiles = []
with open('advent2020/20/test.txt', 'r') as f:
    raw_tile = []
    for line in f.readlines():
        if line == '\n':
            id = raw_tile[0].split()[1][0:4]
            tiles.append(Tile(id, raw_tile[1:]))
            raw_tile = []
        else:
            raw_tile.append(line.strip())

# for each tile, for remaining tiles
# check borders and add to general match set, per border set
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
                    matches.setdefault(tiles[i].id, [])
                    matches.setdefault(tiles[j].id, [])
                    matches[tiles[i].id].append([tiles[j].id, x, b1==b2])
                    matches[tiles[j].id].append([tiles[i].id, y, b1==b2])
                    #tiles[i].matches.setdefault(tiles[j].id, [])
                    #tiles[i].matches[tiles[j].id].append(y)
                    #tiles[j].matches.setdefault(tiles[i].id, [])
                    #tiles[j].matches[tiles[i].id].append(x)

n = int(sqrt(len(tiles)))
layout = [['' for x in range(n)] for y in range(n)]

corner_inds = [[x, y] for x in [0, n-1] for y in [0, n-1]]
for k,v in matches.items():
    # pick a top-left corner
    if len(v) == 2:
        layout[0][0] = k
        break

k = layout[0][0]
sides = set([m[1] for m in matches[k]])
# rotate corner into place
while len(sides) != len(sides.intersection({1,2})):
    tilemap[k].rotate()
    for m in matches[k]:
        m[1] += 1
    sides = set([m[1] for m in matches[k]])

remaining = set(tilemap.keys())
remaining.remove(k)
#print(tilemap['2311'].trymatch(tilemap['1951'], 2))
for i in range(n):
    for j in range(n):
        while layout[i][j] == '':
            if i == 0:
                r = layout[i][j-1]
                b = 3
            else:
                r = layout[i-1][j]
                b = 0
            pots = [tilemap[x[0]] for x in matches[r]]
            for p in pots:
                if p.trymatch(tilemap[r], b):
                    layout[i][j] = p['id']
                    remaining.remove(p['id'])
            for rem in remaining:
                if tilemap[rem].trymatch(tilemap[r], b):
                    layout[i][j] = rem
                    remaining.remove(rem)


for row in layout:
    print(row)
