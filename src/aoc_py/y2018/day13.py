"""
2018 day 13 - Mine Cart Madness

Store the carts and make them sortable, and keep the grid in a dict to easily be able to find the track for a certain
point.
For part 1, keep moving step-by-step until first collision is registered.
For part 2, keep going until there is only one cart left.
"""

from copy import deepcopy
from typing import Final

from aoc_py.util.point import Directions, Point


class Cart:
    __FACING_MAP: Final = {
        "<": Directions.LEFT,
        ">": Directions.RIGHT,
        "^": Directions.UP,
        "v": Directions.DOWN,
    }

    def __init__(self, point: Point, facing: str) -> None:
        self.__pos = point
        self.__facing: Point = Cart.__FACING_MAP[facing]
        self.__turncount = 0

    def move(self) -> Point:
        self.__pos += self.__facing
        return self.__pos

    def update_rotation(self, track: str) -> None:
        match track:
            case "+":
                if self.__turncount == 0:
                    self.__facing = self.__facing.rotate_left()
                elif self.__turncount == 2:
                    self.__facing = self.__facing.rotate_right()
                self.__turncount = (self.__turncount + 1) % 3
            case "/":
                if self.__facing.y == 0:
                    self.__facing = self.__facing.rotate_left()
                else:
                    self.__facing = self.__facing.rotate_right()
            case "\\":
                if self.__facing.y == 0:
                    self.__facing = self.__facing.rotate_right()
                else:
                    self.__facing = self.__facing.rotate_left()
            case _:
                pass

    def get_pos(self) -> Point:
        return self.__pos

    def __lt__(self, other: Cart) -> bool:
        return self.__pos < other.__pos


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__carts: set[Cart] = set()
        self.__tracks: dict[Point, str] = {}
        for y, line in enumerate(rawstr.splitlines()):
            for x, char in enumerate(line):
                if char in (">", "<", "^", "v"):
                    self.__carts.add(Cart(Point(x, y), char))
                    self.__tracks[Point(x, y)] = "-" if char in ("<", ">") else "|"
                elif char != " ":
                    self.__tracks[Point(x, y)] = char

    def get_p1(self) -> str:
        carts = sorted(deepcopy(self.__carts))
        while True:
            taken: list[Point] = [c.get_pos() for c in carts]
            for i, cart in enumerate(carts):
                newpos = cart.move()
                if newpos in taken:
                    return f"{newpos.x},{newpos.y}"
                else:
                    taken[i] = newpos
                cart.update_rotation(self.__tracks[newpos])
            carts.sort()

    def get_p2(self) -> str:
        carts = sorted(deepcopy(self.__carts))
        while len(carts) > 1:
            taken: list[Point] = [c.get_pos() for c in carts]
            deadcarts: set[int] = set()
            for i, cart in enumerate(carts):
                if i in deadcarts:
                    continue
                newpos = cart.move()
                if newpos in taken:
                    deadcarts.add(i)
                    deadcarts.add(taken.index(newpos))
                else:
                    taken[i] = newpos
                    cart.update_rotation(self.__tracks[newpos])
            carts = sorted([cart for i, cart in enumerate(carts) if i not in deadcarts])
        p = carts[0].get_pos()
        return f"{p.x},{p.y}"


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
