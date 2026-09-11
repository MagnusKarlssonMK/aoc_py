"""
2023 day 23 - A Long Walk

Stores the grid as a graph with the gridpoints connecting to more than two neighbors as vertices. Uses BFS to find
the edges, and then a recursive DFS to calculate all path lengths from start to exit to find the longest path.
An argument can be given when rebuilding the graph to ignore the slopes for part 2. Note that this graph results in
significantly more edges and makes Part 2 take a really long time to complete.
"""

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point


def is_opposite_direction(p: Point, d: str) -> bool:
    opposite_dirmap = {
        "<": Directions.RIGHT,
        ">": Directions.LEFT,
        "^": Directions.DOWN,
        "v": Directions.UP,
    }
    return False if d == "." else p == opposite_dirmap[d]


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

    def __load_tree(self, ignore_slopes: bool):
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
        trim_seen: set[Point] = set()
        while trim_queue:
            node, prev = trim_queue.pop(0)
            remove_me = None
            exit_in_neighbors = self.__exit in [x for x, _ in self.__adj[node]]
            for n, s in self.__adj[node]:
                if n == prev:
                    remove_me = n, s
                elif not exit_in_neighbors and len(self.__adj[n]) < 4:
                    trim_queue.append((n, node))
            if remove_me:
                self.__adj[node].remove(remove_me)
            trim_seen.add(node)

    def __dfs(self, from_v: Point, to_v: Point, seen: set[Point]) -> list[int]:
        if from_v == to_v:
            return [0]
        seen.add(from_v)
        lengthlist: list[int] = []
        for next_v, distance in self.__adj[from_v]:
            if next_v not in seen:
                for length in self.__dfs(next_v, to_v, seen):
                    lengthlist.append(length + distance)
        seen.remove(from_v)
        return lengthlist

    def get_maxpathlength(self, ignore_slopes: bool = False) -> int:
        self.__load_tree(ignore_slopes)
        return max(self.__dfs(self.__start, self.__exit, set()))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_maxpathlength())
    if part in (None, 2):
        p2 = str(p.get_maxpathlength(True))

    return p1, p2
