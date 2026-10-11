"""
2017 day 22 - Sporifica Virus

The grid is stored as a dict mapping a packed (x, y) integer key to a NodeState; keys that are absent are CLEAN. The
virus position is kept as two plain integers and its direction as a (dx, dy) pair, so a burst is only integer
arithmetic and a dict lookup instead of allocating Point objects for the position and for every rotation. Because
part 2 performs 10,000,000 bursts, the burst logic is also inlined into the loop rather than being a method call.
"""

from enum import IntEnum
from typing import Final

# The y coordinate is packed into the low bits of the key. Since the virus only ever moves one step per burst, 2**25
# is comfortably larger than the maximum |y| reachable in 10,000,000 bursts, so the packing is collision free.
_KEY_SHIFT: Final = 25

PART1_BURSTS: Final = 10_000
PART2_BURSTS: Final = 10_000_000


class NodeState(IntEnum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__grid: dict[int, NodeState] = {}
        lines = rawstr.splitlines()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == "#":
                    self.__grid[(x << _KEY_SHIFT) + y] = NodeState.INFECTED
        self.__start = (len(lines) // 2, len(lines[0]) // 2)

    def get_infected_count(self, bursts: int, evolved: bool = False) -> int:
        grid = dict(self.__grid)
        x, y = self.__start
        dx, dy = 0, -1  # Start facing up.
        count = 0
        if not evolved:
            # A clean node becomes infected and an infected node becomes clean, turning left and right respectively.
            for _ in range(bursts):
                key = (x << _KEY_SHIFT) + y
                if key in grid:
                    dx, dy = -dy, dx  # Turn right.
                    del grid[key]
                else:
                    dx, dy = dy, -dx  # Turn left.
                    grid[key] = NodeState.INFECTED
                    count += 1
                x += dx
                y += dy
        else:
            clean, weakened, infected, flagged = NodeState
            get = grid.get
            for _ in range(bursts):
                key = (x << _KEY_SHIFT) + y
                state = get(key, clean)
                if state == clean:
                    dx, dy = dy, -dx  # Turn left.
                    grid[key] = weakened
                elif state == weakened:
                    grid[key] = infected
                    count += 1
                elif state == infected:
                    dx, dy = -dy, dx  # Turn right.
                    grid[key] = flagged
                else:
                    dx, dy = -dx, -dy  # Reverse direction.
                    del grid[key]
                x += dx
                y += dy
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_infected_count(PART1_BURSTS))
    if part in (None, 2):
        p2 = str(p.get_infected_count(PART2_BURSTS, True))

    return p1, p2
