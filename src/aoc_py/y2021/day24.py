"""
2021 day 24 - Arithmetic Logic Unit

The instructions are a bit of a bait to implement an emulator, but that isn't actually very helpful. Instead, we need
to try to reverse engineer what the program is doing. The monad program consists of 14 identical chunks
of instructions with slightly different numbers as arguments, i.e. each chunk represents one calculcation per digit in
the model number.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Final


class Op(Enum):
    INC = 1
    MOD = 2


@dataclass(frozen=True)
class Chunk:
    op: Op
    val: int


class InputData:
    __MIN_DIGIT: Final = 1
    __MAX_DIGIT: Final = 9

    def __init__(self, s: str) -> None:
        self.__monad: list[Chunk] = []
        for chunk in s.strip("inp w\n").split("inp w\n"):
            lines = chunk.splitlines()
            if lines[3][-1] == "1":
                self.__monad.append(Chunk(Op.INC, int(lines[-3].split()[-1])))
            else:
                self.__monad.append(Chunk(Op.MOD, int(lines[4].split()[-1])))

    def get_model_nbr(self, smallest: bool = False) -> int:
        modelnbr = [0 for _, _ in enumerate(self.__monad)]
        buffer: list[tuple[int, int]] = []
        for i, chunk in enumerate(self.__monad):
            match chunk.op:
                case Op.INC:
                    buffer.append((i, chunk.val))
                case Op.MOD:
                    idx, val = buffer.pop()
                    delta = val + chunk.val
                    if not smallest:
                        modelnbr[idx] = (
                            InputData.__MAX_DIGIT
                            if delta < 0
                            else InputData.__MAX_DIGIT - delta
                        )
                        modelnbr[i] = (
                            InputData.__MAX_DIGIT
                            if delta > 0
                            else InputData.__MAX_DIGIT + delta
                        )
                    else:
                        modelnbr[idx] = (
                            InputData.__MIN_DIGIT
                            if delta > 0
                            else InputData.__MIN_DIGIT - delta
                        )
                        modelnbr[i] = (
                            InputData.__MIN_DIGIT
                            if delta < 0
                            else InputData.__MIN_DIGIT + delta
                        )
        return int("".join(map(str, modelnbr)))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_model_nbr())
    if part in (None, 2):
        p2 = str(p.get_model_nbr(True))

    return p1, p2
