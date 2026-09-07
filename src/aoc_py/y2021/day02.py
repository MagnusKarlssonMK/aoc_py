"""
2021 day 2 - Dive!
"""

from dataclasses import dataclass
from enum import Enum

from aoc_py.util.point import Directions, Point


class Move(Enum):
    UP = "up"
    DOWN = "down"
    FORWARD = "forward"


@dataclass(frozen=True)
class Command:
    move: Move
    value: int


class InputData:
    def __init__(self, s: str) -> None:
        self.__instructions = [
            Command(Move(left), int(right))
            for left, right in [line.split() for line in s.splitlines()]
        ]

    def get_p1(self) -> int:
        position = Directions.ORIGIN
        for instr in self.__instructions:
            match instr.move:
                case Move.UP:
                    position += Directions.UP * instr.value
                case Move.DOWN:
                    position += Directions.DOWN * instr.value
                case Move.FORWARD:
                    position += Directions.RIGHT * instr.value
        return position.x * position.y

    def get_p2(self) -> int:
        position = Directions.ORIGIN
        aim = 0
        for instr in self.__instructions:
            match instr.move:
                case Move.UP:
                    aim -= instr.value
                case Move.DOWN:
                    aim += instr.value
                case Move.FORWARD:
                    position += Point(instr.value, aim * instr.value)
        return position.x * position.y


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
