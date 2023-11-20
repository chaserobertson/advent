#!/usr/bin/python3

def valve_str(valve_dict, open):
    pressure = sum([valve_dict[o][0] for o in open])
    if len(open) < 1:
        return "No valves are open."
    elif len(open) == 1:
        return f"Valve {open[0]} is open, releasing {pressure} pressure."
    else:
        open_str = ', '.join(open[:-1])
        return f"Valves {open_str} and {open[-1]} are open, releasing {pressure} pressure."

def choose_path(current, open, useful, valve_dict):
    if useful.issubset(open):
        return []
    
    path = []
    for move in valve_dict[current][1]:
        path = [move] + choose_path(move, open+[move], useful, valve_dict)
    print(path)
    return path

input = []
with open('2022/16/test.txt', 'r') as f:
    input = f.read().splitlines()

valve_dict = {}
useful = set()
for line in input:
    words = line.split()
    name = words[1]
    rate = int(words[4].split('=')[1][:-1])
    leads_to = [w.replace(',', '') for w in words[9:]]
    valve_dict[name] = (rate, leads_to)
    if rate > 0:
        useful.add(name)

open, path = [], []
current = 'AA'
for minute in range(1, 6):
    print(f"== Minute {minute} ==")
    print(valve_str(valve_dict, open))
    if not path and current not in open and valve_dict[current][0] > 0:
        print(f"You open valve {current}.")
        open.append(current)
    else:
        path = choose_path(current, open, useful, valve_dict)
        if path:
            current = path.pop()
            print(f"You move to valve {current}.")
    print()
