"""
2018 day 16 - Chronal Classification

Part 1

Load the opcode functionality into lambda functions mapped in a dict, then for each sample,
run through all opcodes and check which ones result in a matching value. Sum up the number
of samples that have at least 3 matches to get the answer.

Part 2

Play a bit of sudoku to generate the mapping between opcode and number, and then run the
test program to find the value of register 0.
"""

from dataclasses import dataclass

OP_CODES = {
    "addr": lambda op, a, b: op[a] + op[b],
    "addi": lambda op, a, b: op[a] + b,
    "mulr": lambda op, a, b: op[a] * op[b],
    "muli": lambda op, a, b: op[a] * b,
    "banr": lambda op, a, b: op[a] & op[b],
    "bani": lambda op, a, b: op[a] & b,
    "borr": lambda op, a, b: op[a] | op[b],
    "bori": lambda op, a, b: op[a] | b,
    "setr": lambda op, a, b: op[a],
    "seti": lambda op, a, b: a,
    "gtir": lambda op, a, b: 1 if a > op[b] else 0,
    "gtri": lambda op, a, b: 1 if op[a] > b else 0,
    "gtrr": lambda op, a, b: 1 if op[a] > op[b] else 0,
    "eqir": lambda op, a, b: 1 if a == op[b] else 0,
    "eqri": lambda op, a, b: 1 if op[a] == b else 0,
    "eqrr": lambda op, a, b: 1 if op[a] == op[b] else 0,
}


@dataclass(frozen=True)
class Instruction:
    op: int  # opcode
    a: int  # input 1
    b: int  # input 2
    c: int  # output


@dataclass(frozen=True)
class Sample:
    before: list[int]
    after: list[int]
    instr: Instruction

    def get_matching_ops(self) -> list[str]:
        return [
            op
            for op in OP_CODES
            if OP_CODES[op](self.before, self.instr.a, self.instr.b)
            == self.after[self.instr.c]
        ]


class InputData:
    def __init__(self, rawstr: str) -> None:
        samples, testprogram = rawstr.split("\n\n\n")
        self.__testprogram = [
            Instruction(*list(map(int, line.split())))
            for line in testprogram.strip("\n").splitlines()
        ]
        self.__samples: list[Sample] = []
        for sample in samples.split("\n\n"):
            before, instr, after = sample.splitlines()
            _, before = before.rstrip("]").split("[")
            _, after = after.rstrip("]").split("[")
            self.__samples.append(
                Sample(
                    list(map(int, before.split(", "))),
                    list(map(int, after.split(", "))),
                    Instruction(*list(map(int, instr.split()))),
                )
            )

    def get_p1(self) -> int:
        return sum(
            [1 for sample in self.__samples if len(sample.get_matching_ops()) >= 3]
        )

    def get_p2(self) -> int:
        # Create dict of possible opcode candidates for each number
        candidates: dict[int, set[str]] = {}
        for sample in self.__samples:
            for m in sample.get_matching_ops():
                if sample.instr.op not in candidates:
                    candidates[sample.instr.op] = set()
                candidates[sample.instr.op].add(m)
        # Figure out the exact mapping sudoku style
        op_mapping = {}
        while candidates:
            for known_nbr in [c for c in candidates if len(candidates[c]) == 1]:
                op_mapping[known_nbr] = candidates[known_nbr].pop()
                del candidates[known_nbr]
                for val in candidates.values():
                    if op_mapping[known_nbr] in val:
                        val.remove(op_mapping[known_nbr])
        # With the opcodes known, we can now run the program
        registers = [0, 0, 0, 0]
        for instr in self.__testprogram:
            registers[instr.c] = OP_CODES[op_mapping[instr.op]](
                registers, instr.a, instr.b
            )
        return registers[0]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
