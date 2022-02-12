#!/usr/bin/python3

import copy

class Fishnumber():
    def __init__(self, numstr, parent) -> None:
        self.parent = parent
        self.depth = 0 if parent == None else parent.depth+1
        if type(numstr) == int:
            self.num = numstr
        elif numstr[0].isdigit():
            self.num = int(numstr[0])
        else:
            stack = []
            for i in range(len(numstr)):
                c = numstr[i]
                if c == '[':
                    stack.append(c)
                elif c == ']':
                    stack.pop()
                if len(stack) == 1 and c == ',':
                    left = Fishnumber(numstr[1:i], self)
                    right = Fishnumber(numstr[i+1:-1], self)
                    self.num = [left, right]

    def __str__(self) -> str:
        out = ''
        if type(self.num) == int:
            out += ''+str(self.num)
        else:
            out += '['+str(self.num[0])
            out += ','+str(self.num[1])+']'
        #out += 'd'+str(self.depth)
        return out

    def magnitude(self):
        if type(self.num) == int:
            return self.num
        else:
            return (3*self.num[0].magnitude()) + (2*self.num[1].magnitude())

    def add(self, digit, dir):
        #print('add', digit, 'to', self)
        if type(self.num) == int:
            self.num += digit.num
        else:
            self.num[dir].add(digit, dir)

    def passup(self, digit, dir):
        #print('passup', digit, 'to', self, dir)
        if self.parent != None:
            if self == self.parent.num[dir]:
                self.parent.passup(digit, dir)
            else:
                self.parent.num[dir].add(digit, int(not dir))

    def explode(self):
        #print('explode', self)
        if self.parent != None:
            if self == self.parent.num[0]:
                self.parent.num[1].add(self.num[1], 0)
                self.parent.passup(self.num[0], 0)
            else:
                self.parent.num[0].add(self.num[0], 1)
                self.parent.passup(self.num[1], 1)
        self.num = 0

    def split(self):
        #print('split', self)
        left = Fishnumber(self.num // 2, self)
        right = Fishnumber(self.num - left.num, self)
        self.num = [left, right]

    def changedepthfromroot(self, dist):
        self.depth += dist
        if type(self.num) != int:
            for child in self.num:
                child.changedepthfromroot(dist)

    def fishadd(self, fn):
        left = copy.deepcopy(self)
        left.parent = self
        left.changedepthfromroot(1)
        right = Fishnumber(fn, self)
        self.num[0] = left
        self.num[1] = right
        #print('after addition:\t'+str(self))
        self.reduce()

    def seekexplode(self):
        explosion = False
        if type(self.num) == int:
            explosion = False
        elif self.depth > 3:
            self.explode()
            explosion = True
        else:
            for child in self.num:
                if child.seekexplode():
                    explosion = True
                    break
        #if explosion and self.depth == 0:
        #    print('after explode:\t'+str(self))
        return explosion

    def seeksplit(self):
        split = False
        if type(self.num) == int:
            if self.num > 9:
                self.split()
                split = True
        else:
            for child in self.num:
                #print(child)
                if child.seeksplit():
                    split = True
                    break
        #if split and self.depth == 0:
        #    print('after split:\t'+str(self))
        return split

    def reduce(self):
        going = True
        while going:
            while self.seekexplode():
                pass
            going = going and self.seeksplit()
        

input = []
with open('advent2021/18/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

root = Fishnumber(input[0], None)
print(root)

for number in input[1:]:
    root.fishadd(number)

print(root)
print(root.magnitude())