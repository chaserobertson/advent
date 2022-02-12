#!/usr/bin/python3

ingredients = []
allergens = []
with open('advent2020/21/input.txt', 'r') as f:
    for line in f.readlines():
        all_str = line[line.find('(')+10:line.find(')')]
        if line.count(',') > 0:
            allergenz = all_str.split(', ')
        else:
            allergenz = [all_str]
        allergens.append(allergenz)

        ingred = line[:line.find('(')].strip().split()
        ingredients.append(ingred)

allergenmap = dict()
for i in range(len(allergens)):
    for a in allergens[i]:
        allergenmap.setdefault(a, set(ingredients[i]))
        allergenmap[a] = allergenmap[a].intersection(ingredients[i])

atoi = dict()
n = -1
while n != len(atoi):
    n = len(atoi)

    settled = []
    for k,v in allergenmap.items():
        if len(v) == 1:
            atoi.setdefault(k, v.pop())
            settled.append(k)

    for s in settled:
        allergenmap.pop(s)
        settled.remove(s)

    for k,v in atoi.items():
        for j,w in allergenmap.items():
            if v in w:
                w.remove(v)
            
ordered = [atoi[s] for s in sorted(atoi.keys())]
print(','.join(ordered))
