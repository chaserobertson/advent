import pathlib
in_file = pathlib.Path.cwd().joinpath('01', 'input.txt')

TARGET = 2020

with open(in_file) as input:
    lines = input.readlines()

for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        li = int(lines[i])
        lj = int(lines[j])
        if li + lj == TARGET:
            print(li * lj)

for i in range(0, len(lines)):
    for j in range(i, len(lines)):
        for k in range(j, len(lines)):
            li = int(lines[i])
            lj = int(lines[j])
            lk = int(lines[k])
            if li + lj + lk == TARGET:
                print(li * lj * lk)
