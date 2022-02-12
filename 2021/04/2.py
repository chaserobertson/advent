#!/usr/bin/python3

import numpy as np

class Board:
    def __init__(self):
        self.board = []
        self.combos = []

    def add_row(self, row):
        self.board.append(row)
        
    def finalize(self):
        for row in self.board:
            self.combos.append(set(row))
        for col in np.array(self.board).T.tolist():
            self.combos.append(set(col))

    def print(self):
        for row in self.board:
            print(row)
        for combo in self.combos:
            print(combo)
        print()

    def __str__(self):
        s = ''
        for row in self.board:
            s += ' '.join(row)
            s += '\n'
        return s

    def check_win(self, draws):
        for combo in self.combos:
            if len(combo.intersection(draws)) == len(combo):
                return True

    def get_sum(self, draws):
        sum = 0
        for row in self.board:
            for val in row:
                if val not in draws:
                    sum += int(val)
        return sum

inputs = []
boards = []
with open('04/input.txt', 'r') as f:
    first_line = f.readline().strip()
    inputs = first_line.split(',')
    f.readline() # skip second line
    board = Board()
    for line in f.readlines():
        if line.strip() == '':
            board.finalize()
            boards.append(board)
            board = Board()
        else:
            board.add_row(line.strip().split())

def print_boards(boards):
    for board in boards:
        board.print()

print(inputs)
print_boards(boards)

wins = []
for i in range(0, len(inputs)):
    for j in range(0, len(boards)):
        if boards[j].check_win(inputs[:i+1]):
            print('Win')
            print(i, inputs[i], j)
            print( boards[j])
            print(boards[j].get_sum(inputs[:i+1]) * int(inputs[i]))
            wins.append(j)
            if len(set(wins)) == len(boards):
                exit()