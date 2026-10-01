"""
2024 day 16 - Reindeer Maze
"""

from collections import deque
from dataclasses import dataclass
from heapq import heappop, heappush
from typing import Final

from aoc_py.util.grid import Grid
from aoc_py.util.point import Directions, Point

DIRECTION_TO_IDX: Final = {
    Directions.RIGHT: 0,
    Directions.DOWN: 1,
    Directions.LEFT: 2,
    Directions.UP: 3,
}


@dataclass(frozen=True)
class State:
    cost: int
    position: Point
    direction: Point

    def __lt__(self, other: State) -> bool:
        return self.cost < other.cost


class InputData:
    def __init__(self, s: str) -> None:
        self.__maze = Grid(s)
        self.__start = self.__maze.find("S")
        self.__exit = self.__maze.find("E")

    def solve(self) -> tuple[int, int]:
        dist: list[list[int | None]] = [
            [None for _ in range(4)] for _ in range(len(self.__maze.elements))
        ]
        fastest: int | None = None
        dist[self.__maze.get_index(self.__start)][
            DIRECTION_TO_IDX[Directions.RIGHT]
        ] = 0
        exit_idx = self.__maze.get_index(self.__exit)
        queue = []
        heappush(queue, State(0, self.__start, Directions.RIGHT))
        while queue:
            current: State = heappop(queue)
            if current.position == self.__exit:
                fastest = (
                    current.cost if fastest is None else min(fastest, current.cost)
                )
                continue
            pos_idx = self.__maze.get_index(current.position)
            d = dist[pos_idx][DIRECTION_TO_IDX[current.direction]]
            if d is not None and current.cost > d:
                continue

            for newcost, newpos, newdir in [
                (
                    current.cost + 1,
                    current.position + current.direction,
                    current.direction,
                ),
                (
                    current.cost + 1000,
                    current.position,
                    current.direction.rotate_left(),
                ),
                (
                    current.cost + 1000,
                    current.position,
                    current.direction.rotate_right(),
                ),
            ]:
                d = dist[self.__maze.get_index(newpos)][DIRECTION_TO_IDX[newdir]]
                if (
                    (e := self.__maze.get_element(newpos)) != ""
                    and e != "#"
                    and (d is None or newcost < d)
                ):
                    heappush(queue, State(newcost, newpos, newdir))
                    dist[self.__maze.get_index(newpos)][DIRECTION_TO_IDX[newdir]] = (
                        newcost
                    )

        if fastest is None:
            # No solution found at all
            return -1, -1

        queue = deque()
        for d in Directions.NEIGHBORS_STRAIGHT:
            if dist[exit_idx][DIRECTION_TO_IDX[d]] == fastest:
                queue.append((self.__exit, d, fastest))

        best_seats = set()
        while queue:
            p, d, v = queue.popleft()
            best_seats.add(p)
            if p == self.__start:
                continue
            nextstep: list[tuple[Point, Point, int]] = [
                (p - d, d, v - 1),
                (p, d.rotate_left(), v - 1000),
                (p, d.rotate_right(), v - 1000),
            ]
            for np, nd, nv in nextstep:
                ndist = dist[self.__maze.get_index(np)][DIRECTION_TO_IDX[nd]]
                if ndist is not None and ndist == nv:
                    queue.append((np, nd, nv))
                    dist[self.__maze.get_index(np)][DIRECTION_TO_IDX[nd]] = None

        return fastest, len(best_seats)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
