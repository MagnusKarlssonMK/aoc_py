"""
2020 day 12 - Rain Risk

Navigate the ship, tracking either its facing direction (part 1) or a waypoint relative to it
(part 2). Rotations spin whichever of the two is tracked, and forward movement advances the
ship by it; the manhattan distance from the origin is then the answer.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Final

from aoc_py.util.point import Directions, Point


class Action(Enum):
    LEFT = "L"
    RIGHT = "R"
    FORWARD = "F"
    NORTH = "N"
    SOUTH = "S"
    WEST = "W"
    EAST = "E"


@dataclass(frozen=True)
class Instruction:
    action: Action
    value: int


class InputData:
    __DIRECTION_MAP: Final = {
        Action.EAST: Directions.RIGHT,
        Action.SOUTH: Directions.DOWN,
        Action.WEST: Directions.LEFT,
        Action.NORTH: Directions.UP,
    }

    def __init__(self, rawstr: str) -> None:
        self.__instructions = [
            Instruction(Action(line[0]), int(line[1:])) for line in rawstr.splitlines()
        ]

    def __navigate(self, use_waypoint: bool) -> int:
        position = Directions.ORIGIN
        direction = Point(10, -1) if use_waypoint else Directions.RIGHT
        for instr in self.__instructions:
            if instr.action in (Action.LEFT, Action.RIGHT):
                for _ in range(instr.value // 90):
                    direction = (
                        direction.rotate_left()
                        if instr.action == Action.LEFT
                        else direction.rotate_right()
                    )
            elif instr.action == Action.FORWARD:
                position += direction * instr.value
            else:
                move = InputData.__DIRECTION_MAP[instr.action] * instr.value
                if use_waypoint:
                    direction += move
                else:
                    position += move
        return position.manhattan(Directions.ORIGIN)

    def get_p1(self) -> int:
        return self.__navigate(False)

    def get_p2(self) -> int:
        return self.__navigate(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
