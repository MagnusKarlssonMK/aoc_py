"""
2016 day 18 - Like a Rogue

Represent the trap row as binary number where trap=1, safe=0.
Then the state for a tile in the next step will be the XOR of the tiles to the left and right.
So (tiles << 1) ^ (tiles >> 1), and then mask it with the original bitwidth so it doesn't expand
towards the left.
"""

PART1_ROWS = 40
PART2_ROWS = 400_000

TRAP_MAP = str.maketrans("^.", "10")


class InputData:
    def __init__(self, s: str) -> None:
        self.__startrow = s

    def get_safetile_count(self, rows: int) -> int:
        nbr_tiles = len(self.__startrow)
        current = int(self.__startrow.translate(TRAP_MAP), 2)
        mask = (1 << nbr_tiles) - 1
        safe_tiles = nbr_tiles - current.bit_count()
        for _ in range(rows - 1):
            current = ((current << 1) ^ (current >> 1)) & mask
            safe_tiles += nbr_tiles - current.bit_count()
        return safe_tiles


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_safetile_count(PART1_ROWS))
    if part in (None, 2):
        p2 = str(p.get_safetile_count(PART2_ROWS))

    return p1, p2
