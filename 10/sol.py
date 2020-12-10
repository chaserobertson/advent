import pathlib
import math

in_file = pathlib.Path.cwd().joinpath('10', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

# cast to ints
adapters = [int(line) for line in lines]
# outlet is 0 jolts
adapters.append(0)
# in ascending order
adapters.sort()

# my device is 3 jolts greater than max adapter
my_device = max(adapters) + 3
adapters.append(my_device)

print('part 1')
jolt_diffs_1 = 0
jolt_diffs_3 = 0
# remember previous adapter joltage
previous = adapters[0]
for adapter in adapters[1:]:
    if adapter - previous == 1:
        jolt_diffs_1 += 1
    elif adapter - previous == 3:
        jolt_diffs_3 += 1
    else:
        print(str([previous, adapter]) + ' confusion!')
    previous = adapter

print([jolt_diffs_1, jolt_diffs_3])
print(str(jolt_diffs_1 * jolt_diffs_3))


print('part 2')


def factor(fac):
    if fac < 3:
        return 0
    elif fac == 3:
        return 1
    else:
        return (2 * factor(fac - 1)) + (fac - 3)


diffs = [adapters[i] - adapters[i-1] for i in range(1, len(adapters))]
print(str(diffs))

windows = []
window = []
for diff in diffs:
    if diff == 3:
        if len(window) > 1:
            windows.append(window[:-1])
        window = []
    else:
        window.append(diff)

print(windows)
pots = []
for win in windows:
    all_poss = 2**len(win)
    imposs = factor(len(win))
    pots.append(all_poss - imposs)
print(pots)
print(math.prod(pots))
