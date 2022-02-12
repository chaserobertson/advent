import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('11', 'input.txt')

FLOOR = '.'
EMPTY = 'L'
OCCUPIED = '#'
NEIGHBORS = 4
NEIGHBORS2 = 5

with open(in_file) as input:
    lines = input.readlines()
lines = [line[:-1] for line in lines]


class Layout:
    def __init__(self, lines):
        self.state = []
        for line in lines:
            self.state.append(line)

    def __eq__(self, obj):
        obj_state = obj.state
        for i in range(0, len(self.state)):
            row1 = self.state[i]
            row2 = obj_state[i]
            for j in range(0, len(row1)):
                seat1 = row1[j]
                seat2 = row2[j]
                if seat1 != seat2:
                    return False
        return True

    def occupiedSeats(self):
        num_seats = 0
        for row in self.state:
            for seat in row:
                if seat == OCCUPIED:
                    num_seats += 1
        return num_seats

    def print(self):
        for row in self.state:
            print(row)

    def nextState(self):
        new_lines = []
        for i in range(0, len(self.state)):
            row = self.state[i]
            new_line = ''
            for j in range(0, len(row)):
                seat = row[j]
                if seat == EMPTY and self.occupiedAdjacentv2(i, j) == 0:
                    new_line += OCCUPIED
                elif seat == OCCUPIED and self.occupiedAdjacentv2(i, j) >= NEIGHBORS2:
                    new_line += EMPTY
                else:
                    new_line += seat
            new_lines.append(new_line)
        next_state = Layout(new_lines)
        return next_state

    def occupiedAdjacent(self, i, j):
        occupied = 0
        mods = [-1, 0, 1]
        for mod_i in mods:
            for mod_j in mods:
                if not (mod_i == 0 and mod_j == 0):
                    i_ind = i + mod_i
                    j_ind = j + mod_j
                    valid_i = i_ind >= 0 and i_ind < len(self.state)
                    valid_j = j_ind >= 0 and j_ind < len(self.state[0])
                    if valid_i and valid_j:
                        if self.state[i_ind][j_ind] == OCCUPIED:
                            occupied += 1
        return occupied

    def occupiedAdjacentv2(self, i, j):
        occupied = 0
        mods = [-1, 0, 1]
        for mod_i in mods:
            for mod_j in mods:
                if not (mod_i == 0 and mod_j == 0):
                    occupied += self.traverse([mod_i, mod_j],
                                              [i + mod_i, j + mod_j])
        return occupied

    def traverse(self, dir, loc):
        oobx = loc[0] < 0 or loc[0] >= len(self.state)
        ooby = loc[1] < 0 or loc[1] >= len(self.state[0])
        if oobx or ooby:
            return 0
        elif self.state[loc[0]][loc[1]] == EMPTY:
            return 0
        elif self.state[loc[0]][loc[1]] == OCCUPIED:
            return 1
        else:
            next_loc = [loc[0] + dir[0], loc[1] + dir[1]]
            return self.traverse(dir, next_loc)


state = Layout(lines)
next = state.nextState()
while state != next:
    state = next
    next = next.nextState()
print(next.occupiedSeats())
