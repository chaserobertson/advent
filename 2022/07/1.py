#!/usr/bin/python3

from anytree import Node, RenderTree, PreOrderIter

class Directory(Node):
    # calculate dir size only if not already cached
    def bytesize(self):
        if not hasattr(self, 'size'):
            self.size = sum([f.bytesize() for f in self.files.values()])
        return self.size

class File(Node):
    # file size is known at creation time
    def bytesize(self):
        return self.size


TOTAL_DISK = 70000000
DIR_SIZE = 100000
NEEDED_DISK = 30000000

input = []
with open('2022/07/input.txt', 'r') as f:
    input = f.read().splitlines()

root = Directory('/', files={})
wd = None
for line in input:
    args = line.split()
    if args[0] == '$':
        if args[1] == 'cd':
            if args[2] == '/':
                wd = root
            elif args[2] == '..':
                wd = wd.parent
            else:
                wd = wd.files[args[2]]
    else:
        name = args[1]
        if args[0] == 'dir':
            wd.files[name] = Directory(name, parent=wd, files={})
        elif args[0].isdigit():
            wd.files[name] = File(name, parent=wd, size=int(args[0]))

# for pre, fill, node in RenderTree(root):
#     print("%s%s %d" % (pre, node.name, s))

available_disk = TOTAL_DISK - root.bytesize()

dirsizes_pt1 = []
dirsizes_pt2 = []
for node in PreOrderIter(root):
    s = node.bytesize()
    if type(node) is Directory and s <= DIR_SIZE:
        dirsizes_pt1.append(s)
    if type(node) is Directory and available_disk + s >= NEEDED_DISK:
        dirsizes_pt2.append(s)

print(sum(dirsizes_pt1))
print(min(dirsizes_pt2))
