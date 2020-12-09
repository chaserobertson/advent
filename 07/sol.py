import pathlib
in_file = pathlib.Path.cwd().joinpath('07', 'input.txt')

# color: string describing name of bag's color
# parents: list of Rules describing bags within
class Rule:
    def __init__(self, color):
        self.color = color
        self.parents = []
        self.children = []
        self.quantities = []

    def __str__(self):
        return 'color: ' + self.color + '\nparents: ' + str(self.parents) + '\nquantities: ' + str(self.quantities)

    def addParent(self, parent, quantity):
        parent.addChild(self, quantity)
        self.parents.append(parent)

    def addChild(self, child, quantity):
        self.children.append(child)
        self.quantities.append(quantity)

    def getAncestors(self):
        ancestors = [self]
        for parent in self.parents:
            ancestors += parent.getAncestors()
        return ancestors

    def getDescendants(self):
        descendants = [self]
        for child in self.children:
            descendants += child.getDescendants()
        return descendants

    def getNumDescendants(self):
        num = 1  # this bag!
        for i in range(0, len(self.children)):
            num += self.quantities[i] * self.children[i].getNumDescendants()
        return num

rules = {}
with open(in_file) as input:
    for line in input.readlines():
        parent, children = line.split(' contain ')
        parent_color = parent.split('bags')[0].strip()
        parent_obj = rules.setdefault(parent_color, Rule(parent_color))
        #parent determined
        #determine children
        if children.strip() == 'no other bags.':
            #continue
            True
        else:
            children_individual = children.split(',')
            for child in children_individual:
                child_actual = child.split('bag')[0].strip()
                child_quant = int(child_actual[0])
                child_color = child_actual[1:].strip()
                # create Rule if not exist, and add this parent to list
                rules.setdefault(child_color, Rule(child_color)).addParent(parent_obj, child_quant)

print('colors that contain shiny gold: ' + str(len(set(rules.get('shiny gold').getAncestors())) - 1))
print('bags required in shiny gold: ' + str(rules.get('shiny gold').getNumDescendants() - 1))