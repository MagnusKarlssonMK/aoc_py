"""
2022 day 12 - Hill Climbing Algorithm

Part 1

Loads the grid into a grid class, and then finding the path is pretty much just a basic BFS, with some extra
condition checks when looking up the neighbors.

Part 2

Similar to Part 1, but this instead does the BFS 'backwards' starting from the end point and also reverses
the condition in the neighbor check.
"""

from collections.abc import Generator

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


class InputData:
    def __init__(self, s: str):
        self.__grid = Grid(s)
        self.__startpos = self.__grid.find("S")
        self.__endpos = self.__grid.find("E")
        self.__grid.set_point(self.__startpos, "a")
        self.__grid.set_point(self.__endpos, "z")

    def getneigbors(self, p: Point, downhill: bool = False) -> Generator[Point]:
        current_val = ord(self.__grid.get_element(p))
        for d in Directions.NEIGHBORS_STRAIGHT:
            neighbor = p + d
            if (neighbor_s := self.__grid.get_element(neighbor)) != "":
                neighbor_val = ord(neighbor_s)
                if (current_val + 1 >= neighbor_val and not downhill) or (
                    current_val <= neighbor_val + 1 and downhill
                ):
                    yield neighbor

    def get_p1(self) -> int:
        # Regular BFS search from S to E
        visited: dict[Point, int] = {}
        tilequeue: list[tuple[Point, int]] = [(self.__startpos, 0)]
        while tilequeue:
            current_pos, current_steps = tilequeue.pop(0)
            if current_pos == self.__endpos:
                return current_steps
            if current_pos in visited:
                continue
            for neighbor in self.getneigbors(current_pos):
                if neighbor not in visited:
                    tilequeue.append((neighbor, current_steps + 1))
            visited[current_pos] = current_steps
        return -1

    def get_p2(self) -> int:
        # BFS again but starting from E and going downhill until finding the first 'a'
        visited: dict[Point, int] = {}
        tilequeue: list[tuple[Point, int]] = [(self.__endpos, 0)]
        while tilequeue:
            current_pos, current_steps = tilequeue.pop(0)
            if self.__grid.get_element(current_pos) == "a":
                return current_steps
            if current_pos in visited:
                continue
            for neighbor in self.getneigbors(current_pos, True):
                if neighbor not in visited:
                    tilequeue.append((neighbor, current_steps + 1))
            visited[current_pos] = current_steps
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
