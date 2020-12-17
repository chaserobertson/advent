import pathlib
import math

in_file = pathlib.Path.cwd().joinpath('14', 'input.txt')

with open(in_file) as input:
    lines = input.readlines()

MASK = 'mask'
MEM = 'mem'
MAX_INT = 68719476735

# for XXXX0XX mask, AND 1111011 (X 0's will stay 0, X 1's will stay 1, 0 will be 0 regardless)
# for XXXX1XX mask, OR 00001100 (X 0's will stay 0, X 1's will stay 1, 1 will be 1 regardless)


class Mask():
    def __init__(self, val):
        self.masks_1 = []
        self.masks_0 = []

        for i in range(0, len(val)):
            char = val[i]
            place = math.pow(2, 35 - i)
            if char == '1':
                self.masks_1.append(int(place))
            elif char == '0':
                self.masks_0.append(MAX_INT - int(place))
            # else do nothing

    def __str__(self):
        output = '1 masks: '
        for mask in self.masks_1:
            output += str(bin(mask)) + ' '
        output += '\n0 masks: '
        for mask in self.masks_0:
            output += str(bin(mask)) + ' '
        return output
        # return str(self.masks_0) + '\n' + str(self.masks_1)

    def apply(self, value):
        new_value = value
        for mask in self.masks_0:
            new_value = new_value.__and__(mask)
        for mask in self.masks_1:
            new_value = new_value.__or__(mask)
        return new_value


mem = {}
masks = []

for line in lines:
    components = line.split(' = ')
    cmd = components[0]
    val = components[1]
    if cmd == MASK:
        masks.append(Mask(val))
    elif cmd[:3] == MEM:
        mem_loc = cmd.split('[')[1].split(']')[0]
        mem[mem_loc] = masks[-1].apply(int(val))

print('part 1')
print(sum(mem.values()))
