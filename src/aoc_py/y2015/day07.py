"""
2015 day 7 - Some Assembly Required

Store the wires in a dict and use operator class to represent gates, then get the answer recursively.
"""

from dataclasses import dataclass
from enum import Enum


class GateType(Enum):
    VALUE = ""
    NOT = "NOT"
    AND = "AND"
    OR = "OR"
    LSHIFT = "LSHIFT"
    RSHIFT = "RSHIFT"


@dataclass
class Gate:
    op: GateType
    value1: str
    value2: str


class InputData:
    def __init__(self, s: str) -> None:
        self.__wires: dict[str, Gate] = {}
        self.__cache: dict[str, int] = {}
        for line in s.splitlines():
            left, right = line.split(" -> ")
            l_tokens = left.split()
            match len(l_tokens):
                case 1:
                    self.__wires[right] = Gate(GateType.VALUE, l_tokens[0], "")
                case 2:
                    self.__wires[right] = Gate(GateType.NOT, l_tokens[1], "")
                case _:
                    self.__wires[right] = Gate(
                        GateType(l_tokens[1]), l_tokens[0], l_tokens[2]
                    )

    def __get_value(self, wire: str) -> int:
        if wire in self.__cache:
            return self.__cache[wire]
        values: list[int] = []
        for v in [self.__wires[wire].value1, self.__wires[wire].value2]:
            if v == "":
                continue
            if v.isdigit():
                values.append(int(v))
            else:
                values.append(self.__get_value(v))
        retval = 0
        match self.__wires[wire].op:
            # Mask with 0xFFFF where necessary to enforce 16-bit behavior
            case GateType.VALUE:
                retval = values[0]
            case GateType.NOT:
                retval = (~values[0]) & 0xFFFF
            case GateType.AND:
                retval = values[0] & values[1]
            case GateType.OR:
                retval = values[0] | values[1]
            case GateType.LSHIFT:
                retval = (values[0] << values[1]) & 0xFFFF
            case GateType.RSHIFT:
                retval = values[0] >> values[1]
        self.__cache[wire] = retval
        return retval

    def get_a_wire_values(self) -> tuple[int, int]:
        p1 = self.__get_value("a")
        self.__cache.clear()
        self.__cache["b"] = p1
        p2 = self.__get_value("a")
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_a_wire_values()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
