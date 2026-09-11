"""
2020 day 24 - Lobby Layout

Similar to the hexgrid problem in 2017 day 11, but using pointy top hex tiles rather than flat top.

Stores the hexgrid using axial coordinate system, i.e. based on 3d system (q, r, s) but with the third dimension
truncated, since the sum of all three must be zero, meaning that it can be calculated when necessary.

Parse each line of instructions into a list of directions, which can then be used to move a point starting from the
reference point (0, 0), and then flip the destination tile, i.e. add to list of black tiles if not there already,
otherwise remove it.

For part 2, it's simply game of life again. For each round, check the neighbors of all black tiles and determine
whether to flip it to white, and also store any white neigbors and check them afterward to see which ones to flip to
black.
"""

from typing import Final

from aoc_py.util.point import Point

# Use the Point class to represent Hex coordinates in axial form (pointy top hex tiles)
# x = q, y = r


class HexDirections:
    NE: Final = Point(1, -1)
    E: Final = Point(1, 0)
    SE: Final = Point(0, 1)
    SW: Final = Point(-1, 1)
    W: Final = Point(-1, 0)
    NW: Final = Point(0, -1)

    NEIGHBORS: Final = [NE, E, SE, SW, W, NW]


class InputData:
    __STR_TO_POINT: Final = {
        "ne": HexDirections.NE,
        "e": HexDirections.E,
        "se": HexDirections.SE,
        "sw": HexDirections.SW,
        "w": HexDirections.W,
        "nw": HexDirections.NW,
    }

    def __init__(self, rawstr: str) -> None:
        self.__move_instr: list[list[Point]] = []
        for line in rawstr.splitlines():
            self.__move_instr.append([])
            i = 0
            while i < len(line):
                if line[i] in self.__STR_TO_POINT:
                    self.__move_instr[-1].append(self.__STR_TO_POINT[line[i]])
                    i += 1
                else:
                    self.__move_instr[-1].append(self.__STR_TO_POINT[line[i : i + 2]])
                    i += 2
        self.__black_tiles: set[Point] = set()

    def get_p1(self) -> int:
        for instr in self.__move_instr:
            tile = Point(0, 0)
            for move in instr:
                tile += move
            if tile in self.__black_tiles:
                self.__black_tiles.remove(tile)
            else:
                self.__black_tiles.add(tile)
        return len(self.__black_tiles)

    def get_p2(self, days: int = 100) -> int:
        for _ in range(days):
            black_tiles: set[Point] = set()
            white_neighbors: set[Point] = set()
            for tile in self.__black_tiles:
                b = 0
                for n in [tile + d for d in HexDirections.NEIGHBORS]:
                    if n in self.__black_tiles:
                        b += 1
                    else:
                        white_neighbors.add(n)
                if 1 <= b <= 2:
                    black_tiles.add(tile)
            for tile in white_neighbors:
                if (
                    sum(
                        [
                            1
                            for n in [tile + d for d in HexDirections.NEIGHBORS]
                            if n in self.__black_tiles
                        ]
                    )
                    == 2
                ):
                    black_tiles.add(tile)
            self.__black_tiles = black_tiles
        return len(self.__black_tiles)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
