#!/usr/bin/python3

from math import prod

class Beacon():
    def __init__(self, bstr):
        a = bstr.strip().split(',')
        self.x = int(a[0])
        self.y = int(a[1])

    def __str__(self):
        return str((self.x, self.y))

    def diff(self, other):
        return prod([pow(self.x-other.x, 2), pow(self.y-other.y, 2)])

class Scanner():
    def __init__(self, scanstr):
        self.id = scanstr[0].split()[2]
        self.beacons = [Beacon(x) for x in scanstr[1:]]

    def __str__(self):
        out = 'Scanner '+self.id
        for b in self.beacons:
            out += '\n'+str(b)
        return out+'\n'

    def difflist(self):
        l = []
        for i in range(len(self.beacons)):
            for j in range(i+1, len(self.beacons)):
                l.append(self.beacons[j].diff(self.beacons[i]))
        return l

    def overlap(self, other):
        x = set(self.difflist())
        y = set(other.difflist())
        ol = len(x.intersection(y))
        return ol

scanners = []
with open('advent2021/19/input.txt', 'r') as f:
    scannerlines = []
    for line in f.readlines():
        if line == '\n':
            scanners.append(Scanner(scannerlines))
            scannerlines = []
        else:
            scannerlines.append(line.strip())

total = 0
for i in range(len(scanners)):
    for j in range(i+1, len(scanners)):
        print(i, j, scanners[i].overlap(scanners[j]))
