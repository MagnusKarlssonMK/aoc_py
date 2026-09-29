"""
2021 day 16 - Packet Decoder

The text description is unfortunately somewhat ambiguous on the decoding of literal values with regard
to the padding of zeroes - judging from the examples, what is apparently meant is that the padding only applies
to the last (outer) package, but the description makes it sound like it applies to ANY literal value package. It is
also not clear what 'its' is referring to - the value or the (sub)package? Or the entire bitstream from the start?

The input is expected to be a single, complete and well formed transmission. A length delimited region
that declares more bits than the stream holds is taken to include the trailing padding, so the region is
clamped to the end of the stream - without that clamp the decode of such a packet would never terminate.
"""

from enum import Enum
from math import prod
from typing import Final


class PacketType(Enum):
    SUM = 0
    PRODUCT = 1
    MIN = 2
    MAX = 3
    LITERAL_VALUE = 4
    GT = 5
    LT = 6
    EQ = 7


class Packet:
    def __init__(self, version: int, packet_type: PacketType, val: int = -1) -> None:
        self.version: int = version
        self.packet_type: PacketType = packet_type
        self.literal_value: int = (
            val if self.packet_type == PacketType.LITERAL_VALUE else -1
        )
        self.subpackets: list[Packet] = []

    def add_subpacket(self, newpacket: Packet) -> None:
        self.subpackets.append(newpacket)

    def get_value(self) -> int:
        if self.packet_type == PacketType.LITERAL_VALUE:
            return self.literal_value
        else:
            match self.packet_type:
                case PacketType.SUM:
                    return sum([sp.get_value() for sp in self.subpackets])
                case PacketType.PRODUCT:
                    return prod([sp.get_value() for sp in self.subpackets])
                case PacketType.MIN:
                    return min([sp.get_value() for sp in self.subpackets])
                case PacketType.MAX:
                    return max([sp.get_value() for sp in self.subpackets])
                case PacketType.GT:
                    return (
                        1
                        if self.subpackets[0].get_value()
                        > self.subpackets[1].get_value()
                        else 0
                    )
                case PacketType.LT:
                    return (
                        1
                        if self.subpackets[0].get_value()
                        < self.subpackets[1].get_value()
                        else 0
                    )
                case PacketType.EQ:
                    return (
                        1
                        if self.subpackets[0].get_value()
                        == self.subpackets[1].get_value()
                        else 0
                    )


HEX_MAP: Final = {
    "0": "0000",
    "1": "0001",
    "2": "0010",
    "3": "0011",
    "4": "0100",
    "5": "0101",
    "6": "0110",
    "7": "0111",
    "8": "1000",
    "9": "1001",
    "A": "1010",
    "B": "1011",
    "C": "1100",
    "D": "1101",
    "E": "1110",
    "F": "1111",
}


class InputData:
    def __init__(self, hexstream: str) -> None:
        self.__bitstream = "".join([HEX_MAP[c] for c in hexstream])
        self.versionsum: int = 0

    def __decode_packet(self, startidx: int) -> tuple[Packet, int]:
        head = startidx
        version = int(self.__bitstream[head : head + 3], 2)
        packet_type = int(self.__bitstream[head + 3 : head + 6], 2)
        head += 6
        self.versionsum += version
        if packet_type == 4:
            value, head = self.__decode_value(head)
            return Packet(version, PacketType.LITERAL_VALUE, value), head
        else:
            length_type = int(self.__bitstream[head])
            head += 1
            newpacket = Packet(version, PacketType(packet_type))
            if length_type == 0:
                subpacket_length = int(self.__bitstream[head : head + 15], 2)
                head += 15
                endidx = min(head + subpacket_length, len(self.__bitstream))
                while head < endidx:
                    subpacket, head = self.__decode_packet(head)
                    newpacket.add_subpacket(subpacket)
            else:
                subpacket_count = int(self.__bitstream[head : head + 11], 2)
                head += 11
                for _ in range(subpacket_count):
                    subpacket, head = self.__decode_packet(head)
                    newpacket.add_subpacket(subpacket)
            return newpacket, head

    def __decode_value(self, startidx: int) -> tuple[int, int]:
        head = startidx
        valuestr = ""
        while True:
            prefix = int(self.__bitstream[head])
            valuestr += self.__bitstream[head + 1 : head + 5]
            head += 5
            if prefix == 0:
                break
        return int(valuestr, 2), head

    def decodestream(self) -> Packet:
        self.versionsum = 0
        packet, _ = self.__decode_packet(0)
        return packet


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    decoder = InputData(inputdata)
    p = decoder.decodestream()
    if part in (None, 1):
        p1 = str(decoder.versionsum)
    if part in (None, 2):
        p2 = str(p.get_value())

    return p1, p2
