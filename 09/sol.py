import pathlib
in_file = pathlib.Path.cwd().joinpath('09', 'input.txt')

WINDOW_SIZE = 25
invalid_number = -1

with open(in_file) as input:
    lines = input.readlines()

# iterate thru each postamble number
for i in range(WINDOW_SIZE, len(lines)):
    target = int(lines[i])
    hasSum = False
    # iterate thru each preamble number
    for j in range(i - WINDOW_SIZE, i):
        # iterate thru each remaining preamble number
        for k in range(j, i):
            lj = int(lines[j])
            lk = int(lines[k])
            # if preamble numbers sum to postamble number
            if lj + lk == target:
                hasSum = True
    if not hasSum:
        print(target)
        invalid_number = target
        break

for i in range(0, len(lines)):
    sum = int(lines[i])
    for j in range(i+1, len(lines)):
        sum += int(lines[j])
        if sum == invalid_number:
            mini = int(min(lines[i: j+1]))
            maxi = int(max(lines[i: j+1]))
            print(mini + maxi)
            exit
        elif sum > invalid_number:
            continue
