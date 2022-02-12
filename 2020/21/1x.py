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
print(allergenmap)

all_ergens = set()
for x in allergenmap.values():
    all_ergens = all_ergens.union(x)

cnt = 0
for i in ingredients:
    cnt += len([x for x in i if x not in all_ergens])
print(cnt)