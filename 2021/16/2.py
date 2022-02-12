#!/usr/bin/python3
import sys

class Literal():
    def __init__(self, packet):
        bin_value = ''
        for i in range(0, len(packet), 5):
            bin_value += packet[i+1:i+5]
            if packet[i] != '1':
                if i+5 < len(packet):
                    self.residual = packet[i+5:]
                else:
                    self.residual = ''
                break
        self.value = int(bin_value, 2)
        print('literal created', self.value, self.residual)

    def get_version_sums(self):
        return 0

    def get_value(self, typeid):
        return self.value

    def __str__(self):
        return str(self.value)

class Operator():
    def __init__(self, packet):
        self.subpackets = []
        lengthtypeid = packet[0]
        if lengthtypeid == '0':
            subpacketslength = int(packet[1:16], 2)
            self.operator = 'subpackets length %d' % subpacketslength
            subpackets = packet[16:16+subpacketslength]
            self.subpackets = extractPackets(subpackets)
            self.residual = packet[16+subpacketslength:]
        else:
            subpacketcount = int(packet[1:12], 2)
            self.operator = 'subpackets count %d' % subpacketcount
            residual = packet[12:]
            for i in range(subpacketcount):
                subpackets = extractPackets(residual)
                if subpackets == None:
                    residual = ''
                else:
                    residual = subpackets[-1].residual
                    self.subpackets += subpackets
            self.residual = residual
        print('operator created', list(map(str, self.subpackets)))

    def get_version_sums(self):
        sums = 0
        for packet in self.subpackets:
            sums += packet.get_version_sums()
        return sums

    def get_value(self, typeid):
        value = 0
        if typeid == 0:
            for packet in self.subpackets:
                value += packet.get_value()
        elif typeid == 1:
            value = 1
            for packet in self.subpackets:
                value *= packet.get_value()
        elif typeid == 2:
            value = sys.maxsize
            for packet in self.subpackets:
                pval = packet.get_value()
                if value > pval:
                    value = pval
        elif typeid == 3:
            for packet in self.subpackets:
                pval = packet.get_value()
                if value < pval:
                    value = pval
        elif typeid == 5:
            value = int(self.subpackets[0].get_value() > self.subpackets[1].get_value())
        elif typeid == 6:
            value = int(self.subpackets[0].get_value() < self.subpackets[1].get_value())
        elif typeid == 7:
            print(len(self.subpackets))
            print(self.subpackets[0].packet)
            value = int(self.subpackets[0].get_value() == self.subpackets[1].get_value())
        print('got value', value)
        return value

    def __str__(self):
        out = self.operator
        for subpacket in self.subpackets:
            out += '\n' + str(subpacket)
        return out

class Packet():
    def __init__(self, bin_str):
        self.version = int(bin_str[0:3], 2)
        self.typeid = int(bin_str[3:6], 2)
        contents = bin_str[6:]
        if self.typeid == 4:
            self.packet = Literal(contents)
        else:
            self.packet = Operator(contents)
        self.residual = self.packet.residual
        print('residual', self.residual)

    def get_version_sums(self):
        return self.version + self.packet.get_version_sums()

    def get_value(self):
        return self.packet.get_value(self.typeid)

    def __str__(self) -> str:
        out = ''
        out += 'version %d' % self.version
        out += ', typeid %d' % self.typeid
        out += ', value %s' % self.packet
        return out
   
# given binary string, return first packet and residual binary
def extractPackets(bin_str):
    if len(bin_str) < 1 or int(bin_str, 2) == 0:
        return None
    else:
        packet = Packet(bin_str)
        residual = packet.residual
        next_packet = extractPackets(residual)
        if next_packet == None:
            return [packet]
        else:
            return [packet] + next_packet

def hex_to_bin(hex_str):
    bin_str = ''
    for h in hex_str:
        d = int(h, 16)
        for i in [8, 4, 2, 1]:
            z = str(int((d % (i*2)) / i >= 1))
            bin_str += z
    return bin_str

input = []
with open('16/input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

for hexa in input:
    binary = hex_to_bin(hexa)
    packets = extractPackets(binary)
    print(hexa)
    for packet in packets:
        print(packet)
        print(packet.get_value())
