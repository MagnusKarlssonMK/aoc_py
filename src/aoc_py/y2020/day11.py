"""
2020 day 11 - Seating System

Give every seat an integer index and pre-calculate its neighbours once, either the directly
adjacent seats (part 1) or the first seat in each direction (part 2). After that, just keep
playing rounds until the occupied seats no longer change.
"""

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        lines = rawstr.splitlines()
        xmax, ymax = len(lines[0]) - 1, len(lines) - 1
        seat_index: dict[Point, int] = {}
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "L":
                    seat_index[Point(x, y)] = len(seat_index)
        self.__adj: list[list[int]] = [[] for _ in seat_index]
        self.__los: list[list[int]] = [[] for _ in seat_index]
        for seat, idx in seat_index.items():
            for d in Directions.NEIGHBORS_ALL:
                n = seat + d
                if n in seat_index:
                    self.__adj[idx].append(seat_index[n])
                while 0 <= n.x <= xmax and 0 <= n.y <= ymax:
                    if n in seat_index:
                        self.__los[idx].append(seat_index[n])
                        break
                    n += d

    def __run_until_stable(self, neighbors: list[list[int]], tolerance: int) -> int:
        occupied_chairs: set[int] = set()
        while True:
            buffer: set[int] = set()
            for chair, nbrs in enumerate(neighbors):
                taken = sum(1 for n in nbrs if n in occupied_chairs)
                if chair in occupied_chairs:
                    if taken < tolerance:
                        buffer.add(chair)
                elif taken == 0:
                    buffer.add(chair)
            if buffer == occupied_chairs:
                return len(buffer)
            occupied_chairs = buffer

    def get_p1(self) -> int:
        return self.__run_until_stable(self.__adj, 4)

    def get_p2(self) -> int:
        return self.__run_until_stable(self.__los, 5)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
