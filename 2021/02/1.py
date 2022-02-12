#!/usr/bin/python3

with open('02/input.txt', 'r') as f:
    pos = [0, 0]
    for line in f.readlines():
        cmd, n = line.split()
        n = int(n)
        if cmd == 'forward':
            pos[0] += n
        elif cmd == 'down':
            pos[1] += n
        elif cmd == 'up':
            pos[1] -= n
        else:
            print('BOOBOO')
            break
    print(pos[0] * pos[1])