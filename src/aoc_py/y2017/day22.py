"""
2017 day 22 - Sporifica Virus

Represent the grid with a set of infected points, and store non-clean points in a dict with its state. While performing
the bursts, add the point or update its state if the point the virus is on is no longer clean, or remove it from the
dict if it becomes clean.
"""

from copy import deepcopy
from enum import Enum

from aoc_py.util.point import Directions, Point


class NodeState(Enum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__infected: dict[Point, NodeState] = {}
        lines = rawstr.splitlines()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    self.__infected[Point(x, y)] = NodeState.INFECTED
        self.__virus_pos: Point = Point(len(lines) // 2, len(lines[0]) // 2)
        self.__virus_dir = Directions.UP
        self.__startvalues = (
            deepcopy(self.__infected),
            deepcopy(self.__virus_pos),
            deepcopy(self.__virus_dir),
        )

    def __reset(self):
        self.__infected = deepcopy(self.__startvalues[0])
        self.__virus_pos = deepcopy(self.__startvalues[1])
        self.__virus_dir = deepcopy(self.__startvalues[2])

    def __perform_burst(self) -> bool:
        current_infected: bool = self.__virus_pos in self.__infected
        if current_infected:
            self.__virus_dir = self.__virus_dir.rotate_right()
            self.__infected.pop(self.__virus_pos)
        else:
            self.__virus_dir = self.__virus_dir.rotate_left()
            self.__infected[self.__virus_pos] = NodeState.INFECTED
        self.__virus_pos += self.__virus_dir
        return not current_infected

    def __perform_evolved_burst(self) -> bool:
        current_state = self.__infected.get(self.__virus_pos, NodeState.CLEAN)
        newstate = None
        match current_state:
            case NodeState.CLEAN:
                self.__virus_dir = self.__virus_dir.rotate_left()
                newstate = NodeState.WEAKENED
            case NodeState.WEAKENED:
                newstate = NodeState.INFECTED
            case NodeState.INFECTED:
                self.__virus_dir = self.__virus_dir.rotate_right()
                newstate = NodeState.FLAGGED
            case NodeState.FLAGGED:
                self.__virus_dir = self.__virus_dir.rotate_right().rotate_right()
                newstate = NodeState.CLEAN
        if newstate != NodeState.CLEAN:
            self.__infected[self.__virus_pos] = newstate
        else:
            self.__infected.pop(self.__virus_pos)
        self.__virus_pos += self.__virus_dir
        return newstate == NodeState.INFECTED

    def get_infected_count(self, bursts: int, evolved: bool = False) -> int:
        if not evolved:
            result = sum([1 for _ in range(bursts) if self.__perform_burst()])
        else:
            result = sum([1 for _ in range(bursts) if self.__perform_evolved_burst()])
        self.__reset()
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_infected_count(10_000))
    if part in (None, 2):
        p2 = str(p.get_infected_count(10_000_000, True))

    return p1, p2
