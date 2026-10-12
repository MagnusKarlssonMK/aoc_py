"""
2024 day 24 - Crossed Wires

## Part 1

The gate instructions are pushed onto a queue and cycled through, repeatedly ripping out
the ones whose inputs are already known, until the queue is empty. The z-wires are then
shifted into place and combined into the output number.

## Part 2

The circuit is a ripple carry adder, so the four swapped gate outputs can be spotted from
the wiring rules:

- every correct AND gate but the first feeds an OR gate,
- only XOR gates may drive an output, except for an OR gate on the most significant bit,
- a correct OR gate never feeds another OR gate,
- and a correct XOR (past the first) feeds another XOR, which in turn drives the output.
"""

from collections import deque
from enum import StrEnum
from typing import NamedTuple


class Operation(StrEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"

    def process(self, a: int, b: int) -> int:
        match self:
            case Operation.AND:
                return a & b
            case Operation.OR:
                return a | b
            case Operation.XOR:
                return a ^ b


class Gate(NamedTuple):
    in_a: str
    in_b: str
    out: str
    op: Operation


class InputData:
    def __init__(self, rawstr: str) -> None:
        values, gates = rawstr.split("\n\n")
        self.__initial_values: dict[str, int] = {}
        for line in values.splitlines():
            wire, value = line.split(": ")
            self.__initial_values[wire] = int(value)
        self.__gates: list[Gate] = []
        for line in gates.splitlines():
            in_a, op, in_b, _, out = line.split()
            self.__gates.append(Gate(in_a, in_b, out, Operation(op)))

    def get_p1(self) -> int:
        wires = dict(self.__initial_values)
        queue = deque(self.__gates)
        while queue:
            gate = queue.popleft()
            if gate.in_a not in wires or gate.in_b not in wires:
                queue.append(gate)
            else:
                wires[gate.out] = gate.op.process(wires[gate.in_a], wires[gate.in_b])
        z = 0
        for wire, value in wires.items():
            if wire.startswith("z") and wire[1:].isdigit():
                z |= value << int(wire[1:])
        return z

    def get_p2(self) -> str:
        input_types: set[tuple[str, Operation]] = set()
        max_z = "z00"
        for gate in self.__gates:
            input_types.add((gate.in_a, gate.op))
            input_types.add((gate.in_b, gate.op))
            max_z = max(max_z, gate.out)

        swapped: list[str] = []
        for gate in self.__gates:
            match gate.op:
                case Operation.AND:
                    if (
                        gate.in_a != "x00"
                        and gate.in_b != "x00"
                        and (gate.out, Operation.OR) not in input_types
                    ):
                        swapped.append(gate.out)
                case Operation.OR:
                    if (gate.out.startswith("z") and gate.out != max_z) or (
                        gate.out,
                        Operation.OR,
                    ) in input_types:
                        swapped.append(gate.out)
                case Operation.XOR:
                    if gate.in_a.startswith("x") or gate.in_b.startswith("x"):
                        if (
                            gate.in_a != "x00"
                            and gate.in_b != "x00"
                            and (gate.out, Operation.XOR) not in input_types
                        ):
                            swapped.append(gate.out)
                    elif not gate.out.startswith("z"):
                        swapped.append(gate.out)

        return ",".join(sorted(swapped))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = p.get_p2()

    return p1, p2
