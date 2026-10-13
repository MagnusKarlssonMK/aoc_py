"""
2017 day 25 - The Halting Problem

Mostly just a bit of parsing headache. It would probably have been much easier to just manually hard code the input,
but resisting the temptation and using a bit of simple regex instead...
Then just keep track of the cursor position and a bytearray tape of 0/1 values (a zero means a clean slot).
"""

import re
from typing import cast


class InputData:
    def __init__(self, s: str) -> None:
        blocks = s.split("\n\n")
        self.__state: str = cast(list[str], re.findall(r"state (\w).", blocks[0]))[0]
        self.__diag_steps: int = int(cast(list[str], re.findall(r"\d+", blocks[0]))[0])
        self.__process: dict[
            str, list[tuple[int, int, str]]
        ] = {}  # state: ((new_v, direction, new_s) when value is 0, same for value 1)
        for block in blocks[1:]:
            states = cast(list[str], re.findall(r"state (\w).", block))
            nbrs = list(map(int, cast(list[str], re.findall(r"\d+", block))))
            directions = [
                1 if c == "right" else -1
                for c in cast(list[str], re.findall(r"slot to the (\w+).", block))
            ]
            self.__process[states[0]] = [
                (nbrs[1], directions[0], states[1]),
                (nbrs[3], directions[1], states[2]),
            ]

    def get_checksum(self) -> int:
        process = self.__process
        state = self.__state
        steps = self.__diag_steps
        offset = steps  # The cursor moves at most one slot per step.
        tape = bytearray(2 * offset + 1)
        cursor_pos = 0
        ones = 0
        for _ in range(steps):
            idx = cursor_pos + offset
            new_val, cursor_dir, state = process[state][tape[idx]]
            if new_val == 1:
                if tape[idx] == 0:
                    ones += 1
                tape[idx] = 1
            elif tape[idx] == 1:
                tape[idx] = 0
                ones -= 1
            cursor_pos += cursor_dir
        return ones


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_checksum())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
