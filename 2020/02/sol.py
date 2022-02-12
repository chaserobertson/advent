import pathlib
import re


class Password:
    def __init__(self, mini, maxi, letter, text):
        self.min = int(mini)
        self.max = int(maxi)
        self.letter = letter
        self.text = text

    def __str__(self):
        return self.min + '-' + self.max + ' ' + self.letter + ': ' + self.text

    def isValid(self):
        occurences = 0
        for c in self.text:
            if c == self.letter:
                occurences += 1
        return occurences <= self.max and occurences >= self.min

    def isValidv2(self):
        a = self.text[self.min - 1]
        b = self.text[self.max - 1]
        if a == self.letter and b == self.letter:
            return False
        elif a == self.letter:
            return True
        elif b == self.letter:
            return True
        else:
            return False


in_file = pathlib.Path.cwd().joinpath('02', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

pws = []
valids = 0
for line in lines:
    pw = re.split('-| |: |\n', line)
    pw_obj = Password(pw[0], pw[1], pw[2], pw[3])
    pws.append(pw_obj)
    if pw_obj.isValid():
        valids += 1

print('Valids v1: ' + str(valids))

valids = 0
for pw_obj in pws:
    if pw_obj.isValidv2():
        valids += 1

print('Valids v2: ' + str(valids))
