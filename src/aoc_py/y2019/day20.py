"""
2019 day 20 - Donut Maze

- Step 1: Parse the grid into a set of walkable cells and the portal entrances. A corridor cell that has two
  uppercase letters two cells away in any straight direction is the entrance of a portal; the label is read in
  reading order and the entrance is classified as OUTER when it lies on the bounding box of the maze cells.
- Step 2: Build a graph whose nodes are the portal entrances. An edge between two different entrances is a BFS
  path through the open corridors and carries the number of steps; the two sides of the same portal (equal label)
  are joined by a single-step edge that stands for stepping through the portal.
- Step 3: One Dijkstra search finds the shortest path from 'AA' to 'ZZ'. Part 1 stays on a single level; Part 2
  tracks a recursion level: stepping through an inner portal goes one level deeper, through an outer portal one
  level shallower, outer portals cannot be used on level 0 and 'AA'/'ZZ' can only be entered on level 0.
"""

from collections import deque
from dataclasses import dataclass
from enum import Enum
from heapq import heappop, heappush

from aoc_py.util.point import Directions, Point


class PortalType(Enum):
    INNER = 0
    OUTER = 1

    def get_opposite(self) -> PortalType:
        return PortalType.INNER if self == PortalType.OUTER else PortalType.OUTER


@dataclass(frozen=True)
class Portal:
    name: str
    ptype: PortalType

    def __lt__(self, other: Portal) -> bool:  # tie-breaker in the priority queue
        return self.name < other.name


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__walkable: set[Point] = set()
        self.__portals: dict[Point, Portal] = {}
        lines = rawstr.splitlines()

        def ch(x: int, y: int) -> str:
            if 0 <= y < len(lines) and 0 <= x < len(lines[y]):
                return lines[y][x]
            return " "

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == ".":
                    self.__walkable.add(Point(x, y))
        names: dict[Point, str] = {}
        for point in self.__walkable:
            for delta in Directions.NEIGHBORS_STRAIGHT:
                first = ch(point.x + delta.x, point.y + delta.y)
                second = ch(point.x + 2 * delta.x, point.y + 2 * delta.y)
                if first.isupper() and second.isupper():
                    if delta == Directions.RIGHT or delta == Directions.DOWN:
                        names[point] = first + second
                    else:
                        names[point] = second + first
                    break
        min_x = min(p.x for p in self.__walkable)
        max_x = max(p.x for p in self.__walkable)
        min_y = min(p.y for p in self.__walkable)
        max_y = max(p.y for p in self.__walkable)
        for point, name in names.items():
            ptype = (
                PortalType.OUTER
                if point.x in (min_x, max_x) or point.y in (min_y, max_y)
                else PortalType.INNER
            )
            self.__portals[point] = Portal(name, ptype)
        self.__portalmap: dict[Portal, set[tuple[Portal, int]]] = {
            portal: set() for portal in self.__portals.values()
        }
        self.__build_portalmap()

    def __build_portalmap(self) -> None:
        for point, portal in self.__portals.items():
            dist: dict[Point, int] = {point: 0}
            queue: deque[Point] = deque([point])
            while queue:
                current = queue.popleft()
                for nxt in (current + d for d in Directions.NEIGHBORS_STRAIGHT):
                    if nxt in self.__walkable and nxt not in dist:
                        dist[nxt] = dist[current] + 1
                        queue.append(nxt)
            for other, other_portal in self.__portals.items():
                if other == point:
                    continue  # would be a zero-step self-loop
                if other_portal.name == portal.name:
                    continue  # sibling side is reached by stepping through the portal
                if other in dist:
                    self.__portalmap[portal].add((other_portal, dist[other]))
        for portal in self.__portalmap:
            mirror = Portal(portal.name, portal.ptype.get_opposite())
            if mirror in self.__portalmap:
                self.__portalmap[portal].add((mirror, 1))

    def __min_steps(self, recursive: bool) -> int:
        start = Portal("AA", PortalType.OUTER)
        target = Portal("ZZ", PortalType.OUTER)
        maxlevel = len(self.__portalmap) if recursive else 0
        visited: dict[tuple[Portal, int], int] = {(start, 0): 0}
        pqueue: list[tuple[int, int, Portal]] = [(0, 0, start)]
        while pqueue:
            steps, level, current = heappop(pqueue)
            if current == target:
                return steps
            if visited[(current, level)] < steps:
                continue
            for nxt, cost in self.__portalmap[current]:
                newlevel = level
                if recursive and nxt.name == current.name:  # stepping through a portal
                    newlevel = level + (1 if nxt.ptype == PortalType.OUTER else -1)
                    if newlevel < 0 or newlevel > maxlevel:
                        continue
                if nxt == start or (nxt == target and newlevel != 0):
                    continue
                nsteps = steps + cost
                if nsteps < visited.get((nxt, newlevel), 10**9):
                    visited[(nxt, newlevel)] = nsteps
                    heappush(pqueue, (nsteps, newlevel, nxt))
        return -1

    def get_p1(self) -> int:
        return self.__min_steps(False)

    def get_p2(self) -> int:
        return self.__min_steps(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
