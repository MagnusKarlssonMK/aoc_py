"""
2018 day 19 - Go With The Flow

Part 1

Simply emulating the program is enough.

Part 2

The program needs to be optimized here. The problematic area is between lines 2-12 (in my input), which
is doing a divisor-sum loop extremely inefficiently. When the instructions at positions 3, 4 and 7 have the
expected shape (mulr / eqrr / addr), the used registers are extracted from the input and the loop is replaced
by a direct computation; any other program is left to pure emulation.

The same optimization can be used in the common function for both parts, and seems to give quite a large performance
boost also for part 1.
"""

from collections.abc import Callable

_OpFunc = Callable[[list[int], int, int], int]

OP_CODES: dict[str, _OpFunc] = {
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
        prog = self.__program
        # The slow divisor-sum loop is only patched when the program is long enough
        # and the instructions at positions 3, 4 and 7 have the expected shape
        # (the tuples hold the OP_CODES lambda singletons, so identity checks work).
        # Any other program is emulated as-is.
        if (
            len(prog) > 13
            and prog[3][0] is OP_CODES["mulr"]
            and prog[4][0] is OP_CODES["eqrr"]
            and prog[7][0] is OP_CODES["addr"]
        ):
            self.__patchregs: tuple[int, int, int] | None = (
                prog[3][1],
                prog[4][2],
                prog[7][2],
            )
        else:
            self.__patchregs = None

    def get_reg_zero_val(self, startvalue: int = 0) -> int:
        registers = [0] * 6
        registers[0] = startvalue
        patchregs = self.__patchregs
        ip = 0
        while 0 <= ip < len(self.__program):
            registers[self.__ip_reg] = ip
            op, a, b, c = self.__program[ip]
            registers[c] = op(registers, a, b)
            ip = registers[self.__ip_reg] + 1

            # Patching the really slow part of the program - this assumes that the troublesome lines are in the
            # area between lines 2 - 12 in the program, and that __init__ recognized the loop's shape
            if ip == 2 and patchregs is not None and registers[patchregs[0]] != 0:
                patchreg1, patchreg2, patchreg3 = patchregs
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
