"""
2016 day 2 - Bathroom Security

Rather than representing the keypad as a grid, instead build it as an adjacency list, to make it easier to deal with
boundaries.
Might look a bit fancier if rather than manually hardcoding the maps, instead directly copying the text mapping from the
description and then having a parsing function to convert it to the layouts, but isn't quite worth it for such simple
mappings.
"""

from enum import Enum
from typing import Final


class Directions(Enum):
    LEFT = "L"
    RIGHT = "R"
    DOWN = "D"
    UP = "U"


class InputData:
    __LAYOUTS: Final = [
        {
            "1": {Directions.RIGHT: "2", Directions.DOWN: "4"},
            "2": {Directions.LEFT: "1", Directions.RIGHT: "3", Directions.DOWN: "5"},
            "3": {Directions.LEFT: "2", Directions.DOWN: "6"},
            "4": {Directions.UP: "1", Directions.RIGHT: "5", Directions.DOWN: "7"},
            "5": {
                Directions.UP: "2",
                Directions.LEFT: "4",
                Directions.RIGHT: "6",
                Directions.DOWN: "8",
            },
            "6": {Directions.UP: "3", Directions.LEFT: "5", Directions.DOWN: "9"},
            "7": {Directions.UP: "4", Directions.RIGHT: "8"},
            "8": {Directions.LEFT: "7", Directions.UP: "5", Directions.RIGHT: "9"},
            "9": {Directions.LEFT: "8", Directions.UP: "6"},
        },
        {
            "1": {Directions.DOWN: "3"},
            "2": {Directions.RIGHT: "3", Directions.DOWN: "6"},
            "3": {
                Directions.UP: "1",
                Directions.LEFT: "2",
                Directions.RIGHT: "4",
                Directions.DOWN: "7",
            },
            "4": {Directions.LEFT: "3", Directions.DOWN: "8"},
            "5": {Directions.RIGHT: "6"},
            "6": {
                Directions.LEFT: "5",
                Directions.UP: "2",
                Directions.RIGHT: "7",
                Directions.DOWN: "A",
            },
            "7": {
                Directions.LEFT: "6",
                Directions.UP: "3",
                Directions.RIGHT: "8",
                Directions.DOWN: "B",
            },
            "8": {
                Directions.LEFT: "7",
                Directions.UP: "4",
                Directions.RIGHT: "9",
                Directions.DOWN: "C",
            },
            "9": {Directions.LEFT: "8"},
            "A": {Directions.UP: "6", Directions.RIGHT: "B"},
            "B": {
                Directions.LEFT: "A",
                Directions.UP: "7",
                Directions.RIGHT: "C",
                Directions.DOWN: "D",
            },
            "C": {Directions.LEFT: "B", Directions.UP: "8"},
            "D": {Directions.UP: "B"},
        },
    ]

    def __init__(self, s: str) -> None:
        self.__instructions = [[Directions(c) for c in line] for line in s.splitlines()]

    def get_bathroom_code(self, advanced_layout: bool = False) -> str:
        code: list[str] = []
        currentpos = "5"
        layout = InputData.__LAYOUTS[1 if advanced_layout else 0]
        for digit in self.__instructions:
            for step in digit:
                if step in layout[currentpos]:
                    currentpos = layout[currentpos][step]
            code.append(currentpos)
        return "".join(code)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_bathroom_code())
    if part in (None, 2):
        p2 = str(p.get_bathroom_code(True))

    return p1, p2
