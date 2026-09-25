"""
2018 day 18 - Settlers of The North Pole

Game of life with three states instead of two, kind of.
Store the grid as a flat list of small state codes (row-major, with a one-cell border) and update according
to the rules for each passing minute. Keeping the grid as a padded list of ints (rather than a dict of
Points and a per-cell Counter) makes the per-minute update cheap: the neighbor scan is fixed index offsets
with no bounds checks, and the trees/lumberyard totals are counted while the next grid is built.
For part 2 we obviously don't want to brute force a trillion minutes, so instead try to find a cycle. The
grid value appears not to be unique enough for all inputs to use as hash for the seen states and look for
repetitions based on that, so instead key the seen states on the raw grid bytes (the border is a constant
zero, so the flattened bytes uniquely determine the real grid).
"""

from enum import Enum


class State(Enum):
    OPEN = "."
    TREES = "|"
    LUMBERYARD = "#"


class InputData:
    P1_TIME: int = 10
    P2_TIME: int = 1_000_000_000

    def __init__(self, rawstr: str) -> None:
        lines = rawstr.splitlines()
        width = len(lines[0])
        height = len(lines)
        # One-cell border of open (0) cells around the real grid so the neighbor scan can use fixed
        # index offsets with no bounds checks. The border is never updated and is ignored as a neighbor.
        self.__stride = width + 2
        grid = [0] * (self.__stride * (height + 2))
        # OPEN=0, TREES=1, LUMBERYARD=2
        code = {state: i for i, state in enumerate(State)}
        for y, line in enumerate(lines, start=1):
            row = y * self.__stride
            for x, c in enumerate(line, start=1):
                grid[row + x] = code[State(c)]
        self.__grid = grid
        # Precompute the real-cell indices and the eight neighbor offsets.
        self.__cells = [
            y * self.__stride + x
            for y in range(1, height + 1)
            for x in range(1, width + 1)
        ]
        s = self.__stride
        self.__offsets = (-s - 1, -s, -s + 1, -1, 1, s - 1, s, s + 1)
        self.__value = 0

    def __step_minute(self) -> None:
        OPEN, TREES, LUMBERYARD = 0, 1, 2
        grid = self.__grid
        offsets = self.__offsets
        new_grid = grid.copy()
        trees_total = 0
        lumber_total = 0
        for i in self.__cells:
            trees = 0
            lumber = 0
            for offset in offsets:
                neighbor = grid[i + offset]
                if neighbor == TREES:
                    trees += 1
                elif neighbor == LUMBERYARD:
                    lumber += 1
            state = grid[i]
            if state == OPEN:
                if trees >= 3:
                    state = TREES
            elif state == TREES:
                if lumber >= 3:
                    state = LUMBERYARD
            elif lumber == 0 or trees == 0:  # LUMBERYARD
                state = OPEN
            new_grid[i] = state
            if state == TREES:
                trees_total += 1
            elif state == LUMBERYARD:
                lumber_total += 1
        self.__grid = new_grid
        self.__value = trees_total * lumber_total

    def __get_value(self) -> int:
        return self.__value

    def __get_keyval(self) -> bytes:
        return bytes(self.__grid)

    def get_total_resource_value(self) -> tuple[int, int]:
        p1 = p2 = 0
        time = 0
        seen: dict[bytes, tuple[int, int]] = {}
        while True:
            time += 1
            self.__step_minute()
            value = self.__get_value()
            keyval = self.__get_keyval()
            if time == InputData.P1_TIME:
                p1 = value
            if keyval in seen:
                cycle = time - seen[keyval][0]
                offset = time - cycle
                p2_time = offset + ((InputData.P2_TIME - offset) % cycle)
                for v in seen:
                    if seen[v][0] == p2_time:
                        p2 = seen[v][1]
                        break
                break
            else:
                seen[keyval] = time, value
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_total_resource_value()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
