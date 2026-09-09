"""
2020 day 11 - Seating System

Pre-calculate the neighbor seats in all directions for every seat, which is done differently for Part 1 vs Part 2. This
does most of the heavy lifting, so after that just keep playing rounds until the occupied seats no longer changes.
"""

from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__seats_adj: dict[Point, set[Point]] = {}
        self.__seats_first: dict[Point, set[Point]] = {}
        xmax = ymax = 0
        for y, line in enumerate(rawstr.splitlines()):
            ymax = max(y, ymax)
            for x, c in enumerate(line):
                xmax = max(x, xmax)
                if c == "L":
                    self.__seats_adj[Point(x, y)] = set()
                    self.__seats_first[Point(x, y)] = set()
        for seat in self.__seats_adj:
            for d in Directions.NEIGHBORS_ALL:
                if (n := seat + d) in self.__seats_adj:
                    self.__seats_adj[seat].add(n)
        for seat in self.__seats_first:
            for d in Directions.NEIGHBORS_ALL:
                n = seat + d
                while 0 <= n.x <= xmax and 0 <= n.y <= ymax:
                    if n in self.__seats_first:
                        self.__seats_first[seat].add(n)
                        break
                    else:
                        n += d

    def get_steadystate_occupied(self, firstseat: bool = False) -> int:
        tolerance = 4 if not firstseat else 5
        occupied_chairs: set[Point] = set()
        neighborlist = self.__seats_adj if not firstseat else self.__seats_first
        while True:
            buffer: set[Point] = set()
            for chair, neighbors in neighborlist.items():
                taken = sum([1 for n in neighbors if n in occupied_chairs])
                if chair in occupied_chairs:
                    if taken < tolerance:
                        buffer.add(chair)
                else:
                    if taken == 0:
                        buffer.add(chair)
            if buffer == occupied_chairs:
                return len(buffer)
            occupied_chairs = buffer


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_steadystate_occupied())
    if part in (None, 2):
        p2 = str(p.get_steadystate_occupied(True))

    return p1, p2
