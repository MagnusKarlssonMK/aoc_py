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

from math import prod


class InputData:
    def __init__(self, s: str) -> None:
        self.__lines = s.splitlines()
        self.__operations = self.__lines.pop().split()

    def get_p1(self) -> int:
        numbers = [
            list(z) for z in zip(*[[*map(int, line.split())] for line in self.__lines])
        ]

        total = 0
        for i, o in enumerate(self.__operations):
            if o == "+":
                total += sum(numbers[i])
            else:
                total += prod(numbers[i])
        return total

    def get_p2(self) -> int:
        numbers_chars_transposed: list[list[str]] = [
            list(z) for z in zip(*[list(line) for line in self.__lines])
        ]
        # Extra padding added for the next step
        numbers_chars_transposed.append([" ", " ", " ", " "])
        total = 0
        op_idx = 0
        number_buffer: list[int] = []
        for col in numbers_chars_transposed:
            if all(c == " " for c in col):
                if self.__operations[op_idx] == "+":
                    total += sum(number_buffer)
                else:
                    total += prod(number_buffer)
                number_buffer = []
                op_idx += 1
            else:
                number_buffer.append(int("".join(col)))
        return total


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
