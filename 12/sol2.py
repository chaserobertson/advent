#!/usr/local/python3

import pathlib
import re
from sol import Ship

in_file = pathlib.Path.cwd().joinpath('12', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

NORTH = 'N'
SOUTH = 'S'
EAST = 'E'
WEST = 'W'
LEFT = 'L'
RIGHT = 'R'
FORWARD = 'F'
START_LOCATION = [0, 0]  # units east, units north
DIRECTIONS = [EAST, NORTH, WEST, SOUTH]
QUADRANTS = {
    0: [1, 1],
    1: [-1, 1],
    2: [-1, -1],
    3: [1, -1]
}


class WaypointShip(Ship):
    def __init__(self):
        super().__init__()
        self.waypoint = [10, 1]

    def __str__(self):
        return str(self.waypoint) + ', ' + super().__str__()

    def move(self, direction, distance):
        if direction == FORWARD:
            self.moveToWaypoint(distance)
        else:
            self.moves[DIRECTIONS.index(direction)](distance)

    def moveNorth(self, distance):
        self.waypoint[1] += distance

    def moveSouth(self, distance):
        self.waypoint[1] -= distance

    def moveEast(self, distance):
        self.waypoint[0] += distance

    def moveWest(self, distance):
        self.waypoint[0] -= distance

    def moveToWaypoint(self, distance):
        self.location[0] += distance * self.waypoint[0]
        self.location[1] += distance * self.waypoint[1]

    def turn(self, direction, degree):
        quadrant = self.getQuadrant()
        if direction == RIGHT:
            change = degree / 90
        elif direction == LEFT:
            change = -degree / 90
        else:
            print('turn direction bad')
        new_quadrant = (quadrant - change) % 4
        new_waypoint = QUADRANTS[new_quadrant].copy()
        if change % 2 == 0:
            new_waypoint[0] *= abs(self.waypoint[0])
            new_waypoint[1] *= abs(self.waypoint[1])
        else:
            new_waypoint[0] *= abs(self.waypoint[1])
            new_waypoint[1] *= abs(self.waypoint[0])
        self.waypoint = new_waypoint

    def getQuadrant(self):
        east_dir = 1 if self.waypoint[0] > 0 else -1
        north_dir = 1 if self.waypoint[1] > 0 else -1
        dirs = [east_dir, north_dir]
        quad_index = list(QUADRANTS.values()).index(dirs)
        return list(QUADRANTS.keys())[quad_index]


ship = WaypointShip()
print(ship)
for line in lines:
    direction = line[0]
    magnitude = int(line[1:-1])
    ship.act(direction, magnitude)
    print(ship)
