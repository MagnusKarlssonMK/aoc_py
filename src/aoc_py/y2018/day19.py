"""
2018 day 19 - Go With The Flow

Part 1

Simply emulating the program is enough.

Part 2

The program needs to be optimized here. The problematic area is between lines 2-12 (in my input), which
is doing some sort of modulo operation extremely inefficiently. So, insert a piece of code that effectively replaces
those lines and does the same job. I've tried to make it reasonably generic by extracting the used registers from the
input, but it will not work for other inputs if the specific lines in the program doing this work are different.

The same optimization can be used in the common function for both parts, and seems to give quite a large performance
boost also for part 1.
"""

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


class InputData:
    def __init__(self, s: str) -> None:
        lines = s.splitlines()
        self.__ip_reg = int(lines[0].split()[1])
        self.__program = [
            (OP_CODES[op], int(a), int(b), int(c))
            for op, a, b, c in [line.split() for line in lines[1:]]
        ]

    def get_reg_zero_val(self, startvalue: int = 0) -> int:
        registers = [0 for _ in range(6)]
        registers[0] = startvalue
        patchreg1 = self.__program[3][1]
        patchreg2 = self.__program[4][2]
        patchreg3 = self.__program[7][2]
        ip = 0
        while 0 <= ip < len(self.__program):
            registers[self.__ip_reg] = ip
            op, a, b, c = self.__program[ip]
            registers[c] = op(registers, a, b)
            ip = registers[self.__ip_reg] + 1

            # Patching the really slow part of the program - this assumes that the troublesome lines are in the
            # area between lines 2 - 12 in the program
            if ip == 2 and registers[patchreg1] != 0:
                while registers[patchreg1] <= registers[patchreg2]:
                    if registers[patchreg2] % registers[patchreg1] == 0:
                        registers[patchreg3] += registers[patchreg1]
                    registers[patchreg1] += 1
                ip = 13

        return registers[0]


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_reg_zero_val())
    if part in (None, 2):
        p2 = str(p.get_reg_zero_val(1))

    return p1, p2
