#!/usr/local/python3

import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('12', 'smol_input.txt')

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
START_LOCATION = [0, 0]  # units east, units north
DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
DEGREES = [0, 90, 180, 270]


class Ship:
    def __init__(self):
        self.location = START_LOCATION
        self.direction = 0  # DIRECTIONS index
        self.moves = [self.moveEast, self.moveNorth,
                      self.moveWest, self.moveSouth]

    def __str__(self):
        return str(self.location) + ', ' + str(self.direction) + ', ' + str(self.manhattanDistance())

    def manhattanDistance(self):
        return abs(self.location[0]) + abs(self.location[1])

    def act(self, direction, magnitude):
        if direction == RIGHT or direction == LEFT:
            self.turn(direction, magnitude)
        else:
            self.move(direction, magnitude)

    def move(self, direction, distance):
        if direction == FORWARD:
            self.moves[self.direction](distance)
        else:
            self.moves[DIRECTIONS.index(direction)](distance)

    def moveNorth(self, distance):
        self.location[1] += distance

    def moveSouth(self, distance):
        self.location[1] -= distance

    def moveEast(self, distance):
        self.location[0] += distance

    def moveWest(self, distance):
        self.location[0] -= distance

    def turn(self, direction, degree):
        current_degree = DEGREES[self.direction]
        if direction == RIGHT:
            current_degree -= degree
        elif direction == LEFT:
            current_degree += degree
        else:
            print('turn direction bad')
        self.direction = DEGREES.index(current_degree % 360)


def main():

    with open(in_file) as input:
        lines = input.readlines()

    ship = Ship()
    print(ship)
    for line in lines:
        direction = line[0]
        magnitude = int(line[1:-1])
        ship.act(direction, magnitude)
        print(ship)


if __name__ == '__main__':
    main()
