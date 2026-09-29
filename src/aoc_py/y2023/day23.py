"""
2023 day 23 - A Long Walk

Stores the grid as a graph with the gridpoints connecting to more than two neighbors as vertices. Uses BFS to find
the edges, and then a recursive DFS to calculate the longest path from start to exit. An argument can be given when
rebuilding the graph to ignore the slopes for part 2. Note that this graph results in more edges and makes part 2
considerably slower than part 1.
"""

from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

OPPOSITE_DIRMAP: Final = {
    "<": Directions.RIGHT,
    ">": Directions.LEFT,
    "^": Directions.DOWN,
    "v": Directions.UP,
}


def is_opposite_direction(direction: Point, nchar: str) -> bool:
    """Returns True if the tile at `nchar` is a slope facing back against the direction of travel, meaning the
    gardener can't enter it that way."""
    return False if nchar == "." else direction == OPPOSITE_DIRMAP[nchar]


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid = Grid(rawstr)
        self.__start = self.__grid.find(".")
        self.__exit = self.__grid.find(".", True)
        # Find the nodes that connects to more than two other neighbors.
        self.__connectors: set[Point] = set()
        self.__adj: dict[Point, set[tuple[Point, int]]] = {}
        for i, c in enumerate(self.__grid.elements):
            if c == "#":
                continue
            neighbors = 0
            p = self.__grid.get_point(i)
            for n in [p + d for d in Directions.NEIGHBORS_STRAIGHT]:
                if self.__grid.get_element(n) not in ("", "#"):
                    neighbors += 1
            if neighbors > 2:
                self.__connectors.add(p)
        self.__connectors.add(self.__start)
        self.__connectors.add(self.__exit)

    def __load_tree(self, ignore_slopes: bool) -> None:
        """Creates the neighbor list between the connectors."""
        self.__adj.clear()
        for vertex in self.__connectors:
            queue: list[tuple[Point, int]] = [(vertex, 0)]
            seen: set[Point] = set()
            if vertex not in self.__adj:
                self.__adj[vertex] = set()
            while queue:
                point, distance = queue.pop(0)
                if point in seen:
                    continue
                seen.add(point)
                for direction in Directions.NEIGHBORS_STRAIGHT:
                    neighbor = point + direction
                    if (nchar := self.__grid.get_element(neighbor)) not in ("", "#"):
                        if neighbor in self.__connectors and neighbor != vertex:
                            self.__adj[vertex].add((neighbor, distance + 1))
                        elif ignore_slopes or not is_opposite_direction(
                            direction, nchar
                        ):
                            queue.append((neighbor, distance + 1))
        # Optimization - only move 'right' / 'down' when on an outer node, meaning nodes with only 3 neighbors.
        # I.e. make those edges directional so that they don't allow backtracking towards the start, since that would
        # make the path cut itself off from the rest of the map.
        trim_queue: list[tuple[Point, Point]] = [(self.__start, Directions.ORIGIN)]
        while trim_queue:
            node, prev = trim_queue.pop(0)
            remove_me = None
            exit_in_neighbors = any(n == self.__exit for n, _ in self.__adj[node])
            for n, s in self.__adj[node]:
                if n == prev:
                    remove_me = n, s
                elif not exit_in_neighbors and len(self.__adj[n]) < 4:
                    trim_queue.append((n, node))
            if remove_me:
                self.__adj[node].remove(remove_me)

    def __dfs(self, from_v: Point, to_v: Point, seen: set[Point]) -> int:
        if from_v == to_v:
            return 0
        seen.add(from_v)
        longest = 0
        for next_v, distance in self.__adj[from_v]:
            if next_v not in seen:
                longest = max(longest, distance + self.__dfs(next_v, to_v, seen))
        seen.remove(from_v)
        return longest

    def get_maxpathlength(self, ignore_slopes: bool = False) -> int:
        self.__load_tree(ignore_slopes)
        return self.__dfs(self.__start, self.__exit, set())

    def get_p1(self) -> int:
        return self.get_maxpathlength()

    def get_p2(self) -> int:
        return self.get_maxpathlength(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
