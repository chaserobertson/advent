import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('04', 'input.txt')

BIRTH_YEAR = 'byr'
ISSUE_YEAR = 'iyr'
EXP_YEAR = 'eyr'
HEIGHT = 'hgt'
HAIR_COLOR = 'hcl'
EYE_COLOR = 'ecl'
PASSPORT_ID = 'pid'
COUNTRY_ID = 'cid'

ALL_FIELDS = {
    BIRTH_YEAR: r'(19[2-9][0-9]|200[0-2])',
    ISSUE_YEAR: r'20(1[0-9]|20)',
    EXP_YEAR: r'20(2[0-9]|30)',
    HEIGHT: r'1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in',
    HAIR_COLOR: r'#([a-f]|[0-9]){6}',
    EYE_COLOR: r'amb|blu|brn|gry|grn|hzl|oth',
    PASSPORT_ID: r'\d{9}',
    COUNTRY_ID: r'.*'
}


class Passport:
    def __init__(self, lines):
        self.fields = {}
        fields = lines.split(' ')
        for field in fields:
            key, val = field.split(':')
            self.fields.setdefault(key, val)

    def __str__(self):
        return str(self.fields.items())

    def getKeys(self):
        return list(self.fields.keys())

    def hasValidKeys(self):
        if len(self.fields.keys()) == len(ALL_FIELDS.keys()):
            return True
        for key in ALL_FIELDS.keys():
            if key != COUNTRY_ID and key not in self.fields.keys():
                return False
        return True

    def hasValidValues(self):
        valid = True
        for key, val in self.fields.items():
            if not re.fullmatch(ALL_FIELDS[key], val):
                valid = False
        return valid

    def isValid(self):
        return self.hasValidKeys() and self.hasValidValues()


with open(in_file) as input:
    lines = input.readlines()

passports = []
cache = ''
for line in lines:
    if line == '\n' and len(cache) > 0:
        passports.append(Passport(cache.strip()))
        cache = ''
    else:
        cache = cache + line.strip() + ' '

valids_keys = 0
for passport in passports:
    if passport.hasValidKeys():
        valids_keys += 1
print(str(valids_keys) + ' passports with valid keys')

valids = 0
for passport in passports:
    if passport.isValid():
        valids += 1
print(str(valids) + ' fully valid passports')
