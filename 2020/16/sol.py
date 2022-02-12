import pathlib
import re

in_file = pathlib.Path.cwd().joinpath('16', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

rules = []
my_ticket = []
nearby_tickets = []
departure_indices = []

section = 0
for line in lines:
    if line == '\n':
        section += 1
        continue
    if section == 0:
        key, val = line.split(': ')
        if len(key) > 8 and key[:9] == 'departure':
            departure_indices.append(len(rules))
        bounds = val.strip().split(' or ')
        bound_list = []
        for bound in bounds:
            min_b, max_b = bound.split('-')
            bound_list.append([int(min_b), int(max_b)])
        rules.append(bound_list)
    elif section == 1:
        if line[:4] != 'your':
            vals = line.strip().split(',')
            my_ticket = [int(val) for val in vals]
    elif section == 2:
        if line[:6] != 'nearby':
            vals = line.strip().split(',')
            nearby_tickets.append([int(val) for val in vals])


def validRules(value):
    valid_rules = set()
    for i in range(0, len(rules)):
        rule = rules[i]
        for subrule in rule:
            if subrule[0] <= value and value <= subrule[1]:
                valid_rules.add(i)
                continue
    return valid_rules


print('part 1')
errors = []
error_tickets = []
for i in range(0, len(nearby_tickets)):
    ticket = nearby_tickets[i]
    for j in range(0, len(ticket)):
        val = ticket[j]
        if len(validRules(val)) < 1:
            errors.append(val)
            error_tickets.append(i)

print(sum(errors))

print('part 2')


valid_tickets = [
    nearby_tickets[i] for i in range(0, len(nearby_tickets)) if i not in error_tickets]

loc_valid_rules = [set(range(0, len(rules))) for i in range(0, len(rules))]

for ticket in valid_tickets:
    for i in range(0, len(ticket)):
        value = ticket[i]
        valid_rules = validRules(value)
        loc_valid_rules[i].intersection_update(valid_rules)

intersections = loc_valid_rules

locations_rule = [-1 for rule in rules]
processing = True
while (processing):
    processing = False
    for sett in intersections:
        if len(sett) == 1:
            p = list(sett)[0]
            locations_rule[intersections.index(sett)] = p
            for q in intersections:
                if p in q:
                    q.remove(p)
            processing = True

summed = 1
for dep in departure_indices:
    summed *= my_ticket[locations_rule.index(dep)]

print(summed)
