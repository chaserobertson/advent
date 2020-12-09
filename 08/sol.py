import pathlib

in_file = pathlib.Path.cwd().joinpath('08', 'input.txt')

NOP = 'nop'
ACC = 'acc'
JMP = 'jmp'
POS = '+'

class Line:
    def __init__(self, line):
        components = line.split(' ')
        pos = False
        if components[1][0] == POS:
            pos = True
        self.cmd = components[0]
        self.pos = pos
        self.num = int(components[1][1:])
    def __str__(self):
        return self.cmd + ' ' + str(self.pos) + ' ' + self.num
    def toggle(self):
        if self.cmd == JMP:
            self.cmd = NOP
            return True
        elif self.cmd == NOP:
            self.cmd = JMP
            return True
        else:
            return False

lines = []
with open(in_file) as input:
    lines = input.readlines()

line_objs = [Line(line) for line in lines]

for j in range(0, len(lines)):
    if not line_objs[j].toggle():
        continue
    accumulator = 0
    seen = [[] for line in lines]

    i = 0
    step = 1
    seen[i].append(step)
    while i < len(lines) and len(seen[i]) < 2:
        step += 1
        line = line_objs[i]
        if line.cmd == ACC:
            if line.pos:
                accumulator += line.num
            else:
                accumulator -= line.num
        elif line.cmd == JMP:
            if line.pos:
                i += (line.num - 1)
            else:
                i -= (line.num + 1)
        i += 1
        try:
            seen[i].append(step)
        except:
            break

    if i < len(lines):
        line_objs[j].toggle()
    else:
        print('line ' + str(i))
        print('step ' + str(step))
        print('accumulator ' + str(accumulator))
        print('Altered Line: ' + str(j))
        break