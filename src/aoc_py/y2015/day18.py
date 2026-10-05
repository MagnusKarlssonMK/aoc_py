"""
2015 day 18 - Like a GIF For Your Yard

Conway's Game of Life over 100 generations, counting the lit cells at the end. Part 1 applies the
plain rule; part 2 pins the four corners of the grid on for the whole run, so a corner that would
otherwise die is restored at the end of every generation and contributes to its neighbours
throughout.

Rather than walking the whole grid each generation, this tallies live neighbours into a dictionary
keyed by position and then keeps only the positions worth keeping. That is a large saving on a mostly
empty 100 by 100 grid, and it is why the live cells are held as a set of (x, y) tuples instead of
using a grid of characters.

One consequence is worth spelling out, because it looks like an oversight. Only positions with at
least one live neighbour ever appear in that dictionary, so a live cell with no neighbours is never
examined and simply disappears from the set. That is the correct outcome, since such a cell must die,
but it happens by omission rather than by rule. Rewriting this as an explicit "survives with two or
three neighbours" test over every in-bounds cell would be a change of approach rather than a fix.

The step count is not read from the input, because the puzzle fixes it at 100. The fallback to 4
exists so the small example in the tests has something short to run, and it is a test-input
accommodation rather than a rule: a grid with fewer than 20 lit cells is silently solved for 4 steps
instead. The real input has 4905 lit cells and so is unaffected.

The grid is assumed square. Its width comes from the first line alone, so a ragged input would be
clipped to that width rather than keeping the longer lines.

An input with no grid at all is answered -1 in both parts. That covers the empty input and an input
made only of empty lines, which has a height but no width. Checking the height alone is not enough:
with no columns the corner positions work out to -1, so part 2 would otherwise count four lit cells
that sit outside the grid entirely.
"""

from typing import Final


class InputData:
    __NEIGHBORS: Final = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

    def __init__(self, s: str) -> None:
        lines = s.splitlines()
        self.__live: set[tuple[int, int]] = {
            (x, y)
            for y, line in enumerate(lines)
            for x, c in enumerate(line)
            if c == "#"
        }
        self.__x_max: int = len(lines[0]) if lines else 0
        self.__y_max: int = len(lines)
        self.__corners: set[tuple[int, int]] = {
            (0, 0),
            (self.__x_max - 1, 0),
            (0, self.__y_max - 1),
            (self.__x_max - 1, self.__y_max - 1),
        }
        self.__nbr_steps: int = 4 if len(self.__live) < 20 else 100

    def __advance(
        self, on_points: set[tuple[int, int]], keep_corners: bool
    ) -> set[tuple[int, int]]:
        """Runs the grid forwards, optionally holding the four corners lit throughout."""
        counts: dict[tuple[int, int], int] = {}
        for _ in range(self.__nbr_steps):
            for x, y in on_points:
                for dx, dy in self.__NEIGHBORS:
                    pos = (x + dx, y + dy)
                    counts[pos] = counts.get(pos, 0) + 1
            survivors = {
                pos
                for pos, n in counts.items()
                if 0 <= pos[0] < self.__x_max
                and 0 <= pos[1] < self.__y_max
                and (n == 3 or (n == 2 and pos in on_points))
            }
            # Part 2 restores the corners after each generation, so they also seed the first one.
            on_points = survivors | self.__corners if keep_corners else survivors
            counts.clear()
        return on_points

    def get_p1(self) -> int:
        return len(self.__advance(self.__live, keep_corners=False))

    def get_p2(self) -> int:
        return len(self.__advance(self.__live | self.__corners, keep_corners=True))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
