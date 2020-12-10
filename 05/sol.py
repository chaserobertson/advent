import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('05', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()


FB_CHARS = 7
RL_CHARS = 3
FRONT = 'F'
BACK = 'B'
RIGHT = 'R'
LEFT = 'L'
ROWS = range(0, 128)
COLS = range(0, 8)


class BoardingPass:
    def __init__(self, text):
        rows = ROWS
        cols = COLS
        for i in range(0, len(text)):
            ch = text[i]
            if i < FB_CHARS:
                if ch == FRONT:
                    rows = rows[:len(rows) // 2]
                if ch == BACK:
                    rows = rows[len(rows) // 2:]
            else:
                if ch == RIGHT:
                    cols = cols[len(cols) // 2:]
                if ch == LEFT:
                    cols = cols[:len(cols) // 2]
        self.row = rows[0]
        self.col = cols[0]
        self.id = (self.row * 8) + self.col

    def __str__(self):
        return 'row ' + str(self.row) + \
            ', column ' + str(self.col) + \
            ', seat ID ' + str(self.id)


passes = []
ids = {}
max = 0
for line in lines:
    bpass = BoardingPass(line.strip())
    passes.append(bpass)
    ids.setdefault(bpass.id, bpass)
    if bpass.id > max:
        max = bpass.id

print('part 1')
print(max)

print('part 2')
id_list = list(ids.keys())
id_list.sort()
prev = id_list[0]
for i in id_list[1:]:
    if i - prev > 1:
        print(i - 1)
    prev = i
