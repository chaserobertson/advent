#!/usr/bin/python3

def get_pairs(polymer):
    pairs = {}
    for i in range(len(polymer)-1):
        pair = polymer[i:i+2]
        pairs.setdefault(pair, 0)
        pairs[pair] += 1
    return pairs

pairs = {}
rules = {}
with open('14/input.txt', 'r') as f:
    template = f.readline().strip()
    pairs = get_pairs(template)
    blank = f.readline()
    for line in f.readlines():
        rule = line.strip().split()
        value = rule[0][0] + rule[2] + rule[0][1]
        rules.setdefault(rule[0], value)

steps = 40
for step in range(steps):
    new_pairs = {}
    for pair in pairs.keys():
        if pair in rules.keys():
            new_pair = [rules[pair][0:2], rules[pair][1:3]]
            for n in new_pair:
                new_pairs.setdefault(n, 0)
                new_pairs[n] += pairs[pair]
        else:
            new_pairs.setdefault(pair, 0)
            new_pairs[pair] += pairs[pair]
    pairs = new_pairs
    #print('After step %d:' % (step+1), polymer)

char_counts = dict()
for pair in pairs.keys():
    for p in pair:
        char_counts.setdefault(p, 0)
        char_counts[p] += pairs[pair]

char_counts[template[0]] += 1
char_counts[template[-1]] += 1

for k, v in char_counts.items():
    char_counts[k] = v // 2

print(char_counts['B'], char_counts['H'])
print(max(char_counts.values()) - min(char_counts.values()))