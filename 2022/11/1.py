#!/usr/bin/python3

import numpy as np

OPS = {
    '*': lambda x, y: x * y,
    '+': lambda x, y: x + y
}

class Monkey:
    def __init__(self, items, op_list, test, targets):
        self.items = items
        self.op_list = op_list
        self.x, self.op, self.y = op_list
        self.op = OPS[self.op]
        self.test = test
        self.targets = targets
        self.business = 0

    def operation(self, item):
        y = item if self.y == 'old' else int(self.y)
        return self.op(item, y)

    def inspect(self, monkeys, mod=None):
        for item in self.items:
            self.business += 1
            # part 2: no div by 3, overflow prevention
            if mod: 
                item = (self.operation(item)) % mod
            else:
                item = self.operation(item) // 3
            # 0th target if no remainder, otherwise 1st target
            target = self.targets[bool(item % self.test)]
            monkeys[target].items.append(item)
        self.items = []

    def __str__(self):
        #return ' '.join([f'{str(x):20}' for x in [self.items, self.op_list, self.test, self.targets]])
        return '  '+str(self.items)


input = []
with open('2022/11/input.txt', 'r') as f:
    input = f.read().splitlines()

monkeys = []

# Make monkeys out of input text
for i in range(0, len(input), 7):
    id = int(input[i].split()[1].removesuffix(':'))
    items = [int(x.removesuffix(',')) for x in input[i+1].split()[2:]]
    op_list = input[i+2].split()[-3:]
    test = int(input[i+3].split()[-1])
    targets = [int(input[i+x].split()[-1]) for x in [4,5]]
    monkeys.append(Monkey(items, op_list, test, targets))

# product of all mod values makes universal mod to prevent overflow
mod = np.prod([monkey.test for monkey in monkeys])

for round in range(1, 10001):
    for i, monkey in enumerate(monkeys):
        monkey.inspect(monkeys, mod)

top_2 = sorted([monkey.business for monkey in monkeys])[-2:]
print(np.prod(top_2))
