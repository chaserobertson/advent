import pathlib
import math

in_file = pathlib.Path.cwd().joinpath('14', '2_input.txt')

with open(in_file) as input:
    lines = input.readlines()

MASK = 'mask'
MEM = 'mem'
MAX_INT = 68719476735

# for XXXX0XX mask, AND 1111011 (X 0's will stay 0, X 1's will stay 1, 0 will be 0 regardless)
# for XXXX1XX mask, OR 00001100 (X 0's will stay 0, X 1's will stay 1, 1 will be 1 regardless)


class MiniMask():
    def __init__(self)


class Mask:
    def __init__(self, val):
        self.masks_1 = []
        self.masks_1X = []
        self.masks_0X = []
        self.real_masks = []

        for i in range(0, len(val)):
            char = val[i]
            place = math.pow(2, 35 - i)
            if char == '1':
                self.masks_1.append(int(place))
            elif char == 'X':
                self.masks_1X.append(int(place))
                self.masks_0X.append(MAX_INT - int(place))
            # else do nothing

        for mask in self.masks_1:

    def __str__(self):
        output = '1 masks: '
        for mask in self.masks_1:
            output += str(bin(mask)) + ' '
        output += '\nX masks: '
        for mask in self.masks_X:
            output += str(bin(mask)) + ' '
        return output
        # return str(self.masks_0) + '\n' + str(self.masks_1)

    def apply(self, value):
        new_values = []
        for mask in self.real_masks:
            new_values.append(mask.apply(value))
        return new_values


mem = {}
masks = []

for line in lines:
    components = line.split(' = ')
    cmd = components[0]
    val = components[1]
    if cmd == MASK:
        masks.append(Mask(val))
        print(masks[-1])
    elif cmd[:3] == MEM:
        mem_loc = cmd.split('[')[1].split(']')[0]
        mem_locs = masks[-1].apply(int(mem_loc))
        print('mem_locs: ' + str(mem_locs))
        for loc in mem_locs:
            mem[loc] = int(val)

print(sum(mem.values()))
