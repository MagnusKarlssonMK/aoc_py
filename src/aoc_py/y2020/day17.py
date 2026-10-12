"""
2020 day 17 - Conway Cubes

Multidimensional game of life. Cubes are packed into a single integer, one base-256 digit per
coordinate offset by 128 so digits stay non-negative, which turns neighbour lookups into plain
integer addition on sets. Coordinates move by at most 6 over the six steps, so every digit
stays comfortably in range. While checking the neighbours of active cubes, collect the
neighbouring inactive cubes, then check which of those to activate.
"""

from itertools import product

_BASE = 256
_OFFSET = 128


def _encode(coords: tuple[int, ...]) -> int:
    value = 0
    for c in coords:
        value = value * _BASE + c + _OFFSET
    return value


def _encode_delta(delta: tuple[int, ...]) -> int:
    value = 0
    for d in delta:
        value = value * _BASE + d
    return value


_DIRECTIONS = {
    dim: [
        _encode_delta(delta) for delta in product((-1, 0, 1), repeat=dim) if any(delta)
    ]
    for dim in (3, 4)
}


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cubes3: set[int] = set()
        self.__cubes4: set[int] = set()
        for y, line in enumerate(rawstr.splitlines()):
            for x, c in enumerate(line):
                if c == "#":
                    self.__cubes3.add(_encode((x, y, 0)))
                    self.__cubes4.add(_encode((x, y, 0, 0)))

    def __run(self, start: set[int], directions: list[int]) -> int:
        cubes = start
        for _ in range(6):
            empty: set[int] = set()
            buffer: set[int] = set()
            for cube in cubes:
                count = 0
                for delta in directions:
                    nbr = cube + delta
                    if nbr in cubes:
                        count += 1
                    else:
                        empty.add(nbr)
                if 2 <= count <= 3:
                    buffer.add(cube)
            for cube in empty:
                count = 0
                for delta in directions:
                    if cube + delta in cubes:
                        count += 1
                        if count > 3:
                            break
                if count == 3:
                    buffer.add(cube)
            cubes = buffer
        return len(cubes)

    def get_p1(self) -> int:
        return self.__run(self.__cubes3, _DIRECTIONS[3])

    def get_p2(self) -> int:
        return self.__run(self.__cubes4, _DIRECTIONS[4])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
