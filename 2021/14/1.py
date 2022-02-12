#!/usr/bin/python3

def get_pairs(polymer):
    pairs = []
    for i in range(len(polymer)-1):
        pairs.append(polymer[i:i+2])
    return pairs

polymer = ''
rules = {}
with open('14/input.txt', 'r') as f:
    polymer = f.readline().strip()
    blank = f.readline()
    for line in f.readlines():
        rule = line.strip().split()
        value = rule[0][0] + rule[2] + rule[0][1]
        rules.setdefault(rule[0], value)

print('Template:    ', polymer)
#print(rules)

steps = 10
for step in range(steps):
    pairs = get_pairs(polymer)
    new_polymer = ''
    for i in range(len(pairs)):
        pair = pairs[i]
        if i == 0:
            if pair in rules.keys():
                new_polymer += rules[pair]
            else:
                new_polymer += pair
        else:
            if pair in rules.keys():
                new_polymer += rules[pair][1:]
            else:
                new_polymer += pair[1:]
    polymer = new_polymer
    #print('After step %d:' % (step+1), polymer)
counts = {x: polymer.count(x) for x in set(polymer)}
print(max(counts.values()) - min(counts.values()))