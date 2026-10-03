"""
2022 day 23 - Unstable Diffusion

Plays rounds until one passes with no elf moving. Each elf is stored in a dict keyed by position, with an 8-bit mask of
which of its eight neighbouring cells are occupied. A round refreshes every mask, then each elf proposes to step to the
first of the four compass directions whose three cells are all free; the priority order of the directions rotates by
one each round, and proposals that collide are dropped. Part 1 is the number of empty ground tiles in the elves'
bounding box after ten rounds, part 2 the first round in which nothing moved.
"""

from typing import Final

# The eight neighbouring cells as (dx, dy, bit), walking the 3x3 block around an elf in row-major order. The bit set
# when that cell is occupied is 2**(7 - index).
_NEIGHBOR_OFFSETS: Final = (
    (-1, -1, 128),
    (0, -1, 64),
    (1, -1, 32),
    (-1, 0, 16),
    (1, 0, 8),
    (-1, 1, 4),
    (0, 1, 2),
    (1, 1, 1),
)
# The four proposed directions as (mask, dx, dy). A direction is free when the mask ANDed with the elf's neighbour mask
# is zero. The order is the initial priority: North, South, West, East.
_DIRECTIONS: Final = (
    (0b11100000, 0, -1),
    (0b00000111, 0, 1),
    (0b10010100, -1, 0),
    (0b00101001, 1, 0),
)


class InputData:
    def __init__(self, gridinput: str) -> None:
        self.__elves: dict[tuple[int, int], int] = {
            (x, y): 0
            for y, row in enumerate(gridinput.splitlines())
            for x, col in enumerate(row)
            if col == "#"
        }
        self.__directions: list[tuple[int, int, int]] = list(_DIRECTIONS)
        self.__scoretable: dict[int, int] = {0: self.__get_currentscore()}

    def __update_elf_neighbors(self) -> None:
        elves = self.__elves
        for x, y in elves:
            mask = 0
            for dx, dy, bit in _NEIGHBOR_OFFSETS:
                if (x + dx, y + dy) in elves:
                    mask |= bit
            elves[(x, y)] = mask

    def get_roundscore(self, rounds: int) -> int:
        return (
            self.__scoretable[rounds]
            if rounds in self.__scoretable
            else self.__scoretable[len(self.__scoretable) - 1]
        )

    def get_stablerounds(self) -> int:
        return max(self.__scoretable.keys())

    def run_simulation(self) -> None:
        stable = False
        i = 1
        while not stable:
            stable = self.__play_round()
            self.__scoretable[i] = self.__get_currentscore()
            self.__directions.append(self.__directions.pop(0))  # Rotate priority
            i += 1

    def __play_round(self) -> bool:
        self.__update_elf_neighbors()
        elves = self.__elves
        proposed: dict[tuple[int, int], tuple[int, int]] = {}
        conflicts: set[tuple[int, int]] = set()
        for elf in elves:
            mask = elves[elf]
            if mask > 0:
                x, y = elf
                for dm, dx, dy in self.__directions:
                    if mask & dm == 0:
                        target = (x + dx, y + dy)
                        if target in proposed:
                            conflicts.add(target)
                        else:
                            proposed[target] = elf
                        break
        changed = False
        for target, source in proposed.items():
            if target not in conflicts:
                elves[target] = 0
                del elves[source]
                changed = True
        return not changed

    def __get_currentscore(self) -> int:
        elves = self.__elves
        xs = [x for x, _ in elves]
        ys = [y for _, y in elves]
        area = (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1)
        return area - len(elves)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    p.run_simulation()
    if part in (None, 1):
        p1 = str(p.get_roundscore(10))
    if part in (None, 2):
        p2 = str(p.get_stablerounds())

    return p1, p2
