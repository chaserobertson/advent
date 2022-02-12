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

itoa = dict()
ing = ingredients.copy()
alr = allergens.copy()
n = -1
while len(itoa) != n:
    n = len(itoa)
    
    for i in range(len(ing)):
        for j in range(i, len(ing)):
            iset = set(ing[i]).intersection(ing[j])
            aset = set(alr[i]).intersection(alr[j])
            if len(iset) == 1 and len(aset) == 1:
                a_match = aset.pop()
                i_match = iset.pop()
                itoa.setdefault(i_match, a_match)

    for i in range(len(ing)):
        for ingr in ing[i]:
            if ingr in itoa.keys():
                ing[i].remove(ingr)
                if itoa[ingr] in alr[i]:
                    alr[i].remove(itoa[ingr])

print(itoa)

#print(ing)
cnt = 0
for ig in ing:
    cnt += len(ig)
print(cnt)
