"""
2019 day 15 - Oxygen System

- Step 1: Drive the repair droid through the maze using BFS to find the shortest path toward still-unknown tiles,
  recording every probe result (wall / open / oxygen) until no reachable tile remains unknown.
- Step 2: BFS from the start over the non-wall tiles to find the shortest path to the oxygen tile, or -1 if no
  oxygen cell was found. This answers part 1.
- Step 3: BFS from the oxygen cell to the farthest reachable tile for the minute count. This answers part 2.
"""

from enum import Enum
from typing import Final

from aoc_py.util.point import Directions, Point
from aoc_py.y2019.intcode import Intcode, IntResult


class InputCommand(Enum):
    NORTH = 1
    SOUTH = 2
    WEST = 3
    EAST = 4


class DroidStatus(Enum):
    WALL = 0
    OK = 1
    OXYGEN = 2


DIRECTION_MAP: Final = {
    InputCommand.NORTH: Directions.UP,
    InputCommand.SOUTH: Directions.DOWN,
    InputCommand.WEST: Directions.LEFT,
    InputCommand.EAST: Directions.RIGHT,
}


class MazeMap:
    def __init__(self) -> None:
        self.__maze: dict[Point, DroidStatus] = {Directions.ORIGIN: DroidStatus.OK}

    def get_unknown_path(self, from_pos: Point) -> list[InputCommand]:
        queue: list[tuple[Point, Point | None, InputCommand | None]] = [
            (from_pos, None, None)
        ]
        seen: dict[Point, tuple[Point | None, InputCommand | None]] = {}
        while queue:
            current, previous, command = queue.pop(0)
            if current not in self.__maze:
                seen[current] = (previous, command)
                result: list[InputCommand] = []
                while current != from_pos:
                    previous_point, from_command = seen[current]
                    assert previous_point is not None
                    assert from_command is not None
                    current = previous_point
                    result.append(from_command)
                return list(reversed(result))
            if current in seen:
                continue
            elif previous:
                seen[current] = (previous, command)
            for dc, dp in DIRECTION_MAP.items():
                neighbor = current + dp
                if neighbor == previous:
                    continue
                if (
                    neighbor not in self.__maze
                    or self.__maze[neighbor] != DroidStatus.WALL
                ):
                    queue.append((neighbor, current, dc))
        return []

    def add_tile(self, p: Point, v: DroidStatus) -> None:
        self.__maze[p] = v

    def get_shortest_path(self) -> int:
        queue = [(Directions.ORIGIN, 0)]
        seen: set[Point] = set()
        while queue:
            current, steps = queue.pop(0)
            if self.__maze[current] == DroidStatus.OXYGEN:
                return steps
            if current in seen:
                continue
            seen.add(current)
            for d in DIRECTION_MAP.values():
                n = current + d
                if n not in seen and self.__maze[n] != DroidStatus.WALL:
                    queue.append((n, steps + 1))
        return -1

    def get_flood_time(self) -> int:
        oxygen_point = list(self.__maze.keys())[
            list(self.__maze.values()).index(DroidStatus.OXYGEN)
        ]
        steps = 0
        queue = [(oxygen_point, steps)]
        seen: set[Point] = set()
        while queue:
            current, steps = queue.pop(0)
            if current in seen:
                continue
            seen.add(current)
            for d in DIRECTION_MAP.values():
                n = current + d
                if n not in seen and self.__maze[n] != DroidStatus.WALL:
                    queue.append((n, steps + 1))
        return steps


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__cpu = Intcode(list(map(int, rawstr.split(","))))
        self.__maze = MazeMap()

    def __build_maze_map(self) -> None:
        droid_pos = Directions.ORIGIN
        droid_direction = Directions.UP
        input_buffer = []
        while True:
            val, res = self.__cpu.run_program()
            if res == IntResult.WAIT_INPUT:
                if not input_buffer:
                    input_buffer = self.__maze.get_unknown_path(droid_pos)
                if not input_buffer:  # No more reachable unknowns
                    break
                step = input_buffer.pop(0)
                droid_direction = DIRECTION_MAP[step]
                self.__cpu.add_input(step.value)
            elif res == IntResult.OUTPUT:
                self.__maze.add_tile(droid_pos + droid_direction, DroidStatus(val))
                if DroidStatus(val) != DroidStatus.WALL:
                    droid_pos += droid_direction
            else:
                break

    def get_p1(self) -> int:
        self.__cpu.reboot()
        self.__build_maze_map()
        return self.__maze.get_shortest_path()

    def get_p2(self) -> int:
        return self.__maze.get_flood_time()


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1 = p.get_p1()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
