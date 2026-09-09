"""
2020 day 12 - Rain Risk
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
    __DIRECTIONMAP: Final = {
        Action.EAST: Directions.RIGHT,
        Action.SOUTH: Directions.DOWN,
        Action.WEST: Directions.LEFT,
        Action.NORTH: Directions.UP,
    }

    def __init__(self, rawstr: str) -> None:
        self.__instructions = [
            Instruction(Action(line[0]), int(line[1:])) for line in rawstr.splitlines()
        ]

    def get_distance(self, use_waypoint: bool = False) -> int:
        position = Point(0, 0)
        direction = (
            InputData.__DIRECTIONMAP[Action.EAST] if not use_waypoint else Point(10, -1)
        )
        for instr in self.__instructions:
            if instr.action in (Action.LEFT, Action.RIGHT):
                for _ in range(instr.value // 90):
                    direction = (
                        direction.rotate_left()
                        if instr.action == Action.LEFT
                        else direction.rotate_right()
                    )
            elif instr.action in (Action.NORTH, Action.EAST, Action.SOUTH, Action.WEST):
                if not use_waypoint:
                    position += InputData.__DIRECTIONMAP[instr.action] * instr.value
                else:
                    direction += InputData.__DIRECTIONMAP[instr.action] * instr.value
            elif instr.action == Action.FORWARD:
                position += direction * instr.value
        return position.manhattan(Directions.ORIGIN)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_distance())
    if part in (None, 2):
        p2 = str(p.get_distance(True))

    return p1, p2
