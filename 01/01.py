with open('input.txt') as input:
    output = 0
    lines = input.readlines()
    for line in lines:
        if line == 2020:
            output = line
    print(output)