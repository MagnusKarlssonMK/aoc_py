"""
2022 day 17 - Pyroclastic Flow

Pretty much tetris with side controls determined by the jet stream input.
Shapes and grid stored in binary format per row in lists and bitshifted / bitmasked to move and check for overlap.
After every dropped rock, trim the lower part of unreachable rows by flood-filling from above with a simple BFS,
and store number of trimmed rows.
For part 2, the result will eventually enter a cycle after an initial stabilization phase. So, store a hashed value
based on rock index, jet index and current grid for each dropped rock, and then once a cycle is found, the answer
can be derived from the stored information.
As it turns out, a cycle is found even before getting the answer to Part 1, so the same solution can actually be
used for both answers. The solution could be optimized to store the result and get the answer to Part 2 immediately,
but it's already fast enough that it isn't really worth the effort.
Breaking the giant drop_rocks function into smaller pieces would be welcome.
"""

from enum import Enum

from aoc_py.util.point import Directions, Point


class Shape(Enum):
    MINUS = 0
    PLUS = 1
    HOOK = 2
    VER_LINE = 3
    BOX = 4

    def get_binary_shape(self) -> tuple[int, list[int]]:  # width, pattern-mask
        match self:
            case Shape.MINUS:
                return 4, [int("1111", 2)]
            case Shape.PLUS:
                return 3, [int("010", 2), int("111", 2), int("010", 2)]
            case Shape.HOOK:
                return 3, [int("111", 2), int("001", 2), int("001", 2)]
            case Shape.VER_LINE:
                return 1, [int("1", 2) for _ in range(4)]
            case Shape.BOX:
                return 2, [int("11", 2) for _ in range(2)]


class Rock:
    width: int
    pos: Point

    def __init__(self, shape: Shape, x: int, y: int) -> None:
        self.width, self.__pattern = shape.get_binary_shape()
        self.pos = Point(x, y)

    def get_grid_pattern(self, grid_width: int) -> list[int]:
        return [val << grid_width - self.pos.x - self.width for val in self.__pattern]


class InputData:
    def __init__(self, jet_stream: str) -> None:
        self.__jet_stream = [1 if c == ">" else -1 for c in jet_stream]
        self.__cave_width = 7
        self.__grid: list[int] = []
        self.__trimmed_rows = 0
        self.__step_count = 0

    def drop_rocks(self, total_rocks: int) -> int:
        self.__grid = []
        self.__trimmed_rows = 0
        self.__step_count = 0
        seen_states: list[int] = []
        seen_trims: list[tuple[int, int]] = []
        max_height = 0
        for rock_nbr in range(total_rocks):
            current_rock_idx = rock_nbr % len(Shape)
            current_rock = Rock(Shape(current_rock_idx), 2, max_height + 3)
            while True:
                # Move sideways if possible
                x_delta = self.__jet_stream[self.__step_count % len(self.__jet_stream)]
                if (
                    0
                    <= x_delta + current_rock.pos.x
                    <= self.__cave_width - current_rock.width
                ):
                    moved_rock: list[int] = []
                    for idx, x_val in enumerate(
                        current_rock.get_grid_pattern(self.__cave_width)
                    ):
                        if x_delta > 0:
                            moved_rock.append(x_val >> 1)
                        else:
                            moved_rock.append(x_val << 1)
                        if current_rock.pos.y + idx < len(self.__grid) and (
                            self.__grid[current_rock.pos.y + idx] & moved_rock[-1] > 0
                        ):
                            break
                    else:  # If we didn't break the loop, there was no collision - accept the new x-position
                        current_rock.pos = Point(
                            current_rock.pos.x + x_delta, current_rock.pos.y
                        )
                self.__step_count += 1
                # Try to move down; if not possible, lock the rock in place in the grid and break the loop
                if current_rock.pos.y > max_height:
                    current_rock.pos = current_rock.pos + Directions.UP
                else:
                    for idx, x_val in enumerate(
                        current_rock.get_grid_pattern(self.__cave_width)
                    ):
                        if current_rock.pos.y == 0 or (
                            current_rock.pos.y - 1 + idx < len(self.__grid)
                            and (self.__grid[current_rock.pos.y - 1 + idx] & x_val > 0)
                        ):
                            break
                    else:
                        current_rock.pos = current_rock.pos + Directions.UP
                        continue
                    # Couldn't move down - lock it in to the grid
                    for idx, x_val in enumerate(
                        current_rock.get_grid_pattern(self.__cave_width)
                    ):
                        if current_rock.pos.y + idx < len(self.__grid):
                            self.__grid[current_rock.pos.y + idx] |= x_val
                        else:
                            self.__grid.append(x_val)
                    # Trim the grid
                    self.__trim_grid()
                    max_height = len(self.__grid)
                    break
            state = hash(
                (
                    current_rock_idx,
                    self.__step_count % len(self.__jet_stream),
                    tuple(self.__grid),
                )
            )
            if state in seen_states:
                offset: int = seen_states.index(state)
                cycle_len = rock_nbr - offset
                trim_per_cycle = self.__trimmed_rows - seen_trims[offset][0]
                nbr_cycles = (
                    total_rocks - 1 - offset
                ) // cycle_len  # Cached list is zero-indexed, rock counter is not.
                idx = offset + (total_rocks - 1 - offset) % cycle_len
                return (
                    seen_trims[idx][0]
                    + seen_trims[idx][1]
                    + (nbr_cycles * trim_per_cycle)
                )
            seen_states.append(state)
            seen_trims.append((self.__trimmed_rows, len(self.__grid)))
        return self.__trimmed_rows + len(self.__grid)

    def __trim_grid(self) -> None:
        # Floodfill the grid from the top, one row above the highest row to guarantee clear space, and then trim
        # anything below rows we can't reach
        seen: set[tuple[int, int]] = set()
        queue = [(0, len(self.__grid))]
        while queue:
            x, y = queue.pop(0)
            if (x, y) in seen:
                continue
            seen.add((x, y))
            for dx, dy in [
                (-1, 0),
                (1, 0),
                (0, -1),
            ]:  # There should never be a need to go up
                new_x = x + dx
                new_y = y + dy
                if (0 <= new_x < self.__cave_width and new_y > 0) and (
                    new_y >= len(self.__grid)
                    or self.__grid[new_y] & 2 ** (self.__cave_width - new_x - 1) == 0
                ):
                    queue.append((new_x, new_y))
        min_y = min([y for _, y in seen])
        while min_y > 1:
            _ = self.__grid.pop(0)
            self.__trimmed_rows += 1
            min_y -= 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.drop_rocks(2022))
    if part in (None, 2):
        p2 = str(p.drop_rocks(1_000_000_000_000))

    return p1, p2
