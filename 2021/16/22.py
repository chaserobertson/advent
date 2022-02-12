
from dataclasses import dataclass
from io import StringIO
from sys import maxsize

with open('16/input.txt', 'r') as f:
    BITS = f.readline().strip()

TYPE_NAMES = {
    0: "sum",
    1: "prod",
    2: "min",
    3: "max",
    5: "gt",
    6: "lt",
    7: "eq",
}

def _snake(head, tail, text):
    first, *rest = text.splitlines()
    yield head + first
    yield from (tail + line for line in rest)

def _tree_printer(root, children):
    yield root
    if not children:
        return
    *children, last = children
    for child in children:
        yield from _snake('├─', '│ ', str(child))
    yield from _snake('╰─', '  ', str(last))


@dataclass
class Packet:
    version: int
    type_id: int
    value: None

    def get_value(self):
        value = 0     
        if self.type_id == 4:
            value = self.value
        elif self.type_id == 0:
            for subpacket in self.value:
                value += subpacket.get_value()
        elif self.type_id == 1:
            value = 1
            for subpacket in self.value:
                value *= subpacket.get_value()
        elif self.type_id == 2:
            value = maxsize
            for subpacket in self.value:
                v = subpacket.get_value()
                if v < value:
                    value = v
        elif self.type_id == 3:
            for subpacket in self.value:
                v = subpacket.get_value()
                if v > value:
                    value = v
        elif self.type_id == 5:
            value = int(self.value[0].get_value() > self.value[1].get_value())
        elif self.type_id == 6:
            value = int(self.value[0].get_value() < self.value[1].get_value())
        elif self.type_id == 7:
            value = int(self.value[0].get_value() == self.value[1].get_value())
        return value
    def __str__(self):
        if self.type_id == 4:
            return str(self.value)

        return "\n".join(_tree_printer(TYPE_NAMES[self.type_id], self.value))

def decimal(bits):
    return int(bits, 2)

def decode(packet: StringIO):
    version = decimal(packet.read(3))
    type_id = decimal(packet.read(3))

    if type_id == 4:
        value = ''
        while packet.read(1) == '1':
            value += packet.read(4)
        value += packet.read(4)
        return Packet(version, type_id, decimal(value))

    m = packet.read(1)
    if m == '0':
        bit_length = decimal(packet.read(15))
        subpacket = StringIO(packet.read(bit_length))
        subpackets = []
        while subpacket.tell() != bit_length:
            subpackets.append(decode(subpacket))
        return Packet(version, type_id, subpackets)
    elif m == '1':
        npackets = decimal(packet.read(11))

        return Packet(version, type_id, [decode(packet) for _ in range(npackets)])


def hex_to_bin(hex_str):
    bin_str = ''
    for h in hex_str:
        d = int(h, 16)
        for i in [8, 4, 2, 1]:
            z = str(int((d % (i*2)) / i >= 1))
            bin_str += z
    return bin_str

r = decode(StringIO(hex_to_bin(BITS)))
print(r)
print(r.get_value())