#!/usr/bin/python3

with open('02/input.txt', 'r') as f:
    pos = [0, 0, 0] # horpos, depth, aim
    for line in f.readlines():
        cmd, n = line.split()
        n = int(n)
        if cmd == 'forward':
            pos[0] += n
            pos[1] += n * pos[2]
        elif cmd == 'down':
            pos[2] += n
        elif cmd == 'up':
            pos[2] -= n
        else:
            print('BOOBOO')
            break
    print(pos)
    print(pos[0] * pos[1])