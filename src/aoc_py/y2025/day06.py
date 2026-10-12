"""
2025 day 6 - Trash Compactor

A parsing exercise.
Group the input in column groups, separated by empty column so each group gets one
operation ('+' or '*') connected to it.

The difference between part 1 and part 2 is how to then parse the numbers; horizontally or
vertically. Parsing horizontally is done with trivial whitespace splitting. The vertical
numbers are derived by first transposing the input and then treating the empty lines as
separators for the column groups.
"""

from collections.abc import Iterable
from math import prod


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines: list[str] = rawstr.splitlines()
        self.__operations: list[str] = self.__lines.pop().split()

    def __eval_group(self, numbers: Iterable[int], operation: str) -> int:
        return sum(numbers) if operation == "+" else prod(numbers)

    def get_p1(self) -> int:
        numbers = zip(*(map(int, line.split()) for line in self.__lines))
        return sum(
            self.__eval_group(column, operation)
            for column, operation in zip(numbers, self.__operations)
        )

    def get_p2(self) -> int:
        total = 0
        op_idx = 0
        number_buffer: list[int] = []
        transposed: list[tuple[str, ...]] = list(zip(*self.__lines))
        for col in transposed:
            if all(c == " " for c in col):
                total += self.__eval_group(number_buffer, self.__operations[op_idx])
                number_buffer = []
                op_idx += 1
            else:
                number_buffer.append(int("".join(col)))
        return total + self.__eval_group(number_buffer, self.__operations[op_idx])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
