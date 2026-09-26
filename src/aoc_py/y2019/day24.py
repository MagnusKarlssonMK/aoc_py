"""
2019 day 24 - Planet of Discord

- Step 1: Parse the 5x5 grid into a 25-character binary bitmask string (a "1" at bit i means a bug in cell i,
  row-major from the top left). For each of the 25 cells a set of neighbor masks is precomputed, each keyed by
  relative level: level 0 holds the up to four same-level adjacent cells (the center cell is kept as an ordinary
  neighbor here, so part 1 is a plain flat-grid evolution); level -1 holds the single outer-level cell that any
  grid-edge cell connects through; level +1 holds the five inner-level cells that the four cells adjacent to the
  center hole connect through. The center and portal positions are hardcoded because the puzzle grid is always
  5x5.
- Step 2: Part 1 evolves the level-0 masks only, applying the life rules (a bug stays alive with exactly one
  neighbor, an empty cell becomes a bug with one or two neighbors) until a layout repeats, then returns the
  repeated layout's biodiversity rating (the sum of 2^bit for every bug cell).
- Step 3: Part 2 keeps a dict of bug layouts per level, growing it by one level in each direction while the
  outermost levels still hold bugs, and clears the center hole cell on every level. Each cell counts its
  neighbors from all three masks whose level actually exists; after 200 minutes the answer is the total number
  of bugs across all levels.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        lines = rawstr.splitlines()
        cols = len(lines[0])
        self.__startbugs = "".join(
            "1" if c == "#" else "0" for line in lines for c in line
        )
        self.__neighbormasks: dict[
            int, set[tuple[int, str]]
        ] = {}  # bit: relative level, mask
        for i, _ in enumerate(self.__startbugs):
            mask = ["0" for _ in enumerate(self.__startbugs)]
            outermask = ["0" for _ in enumerate(self.__startbugs)]
            innermask = ["0" for _ in enumerate(self.__startbugs)]
            # Left
            if i % cols != 0:
                mask[i - 1] = "1"
                if i - 1 == 12:
                    innermask[4] = innermask[9] = innermask[14] = innermask[
                        19
                    ] = innermask[24] = "1"
            else:
                outermask[11] = "1"
            # Right
            if i % cols != cols - 1:
                mask[i + 1] = "1"
                if i + 1 == 12:
                    innermask[0] = innermask[5] = innermask[10] = innermask[
                        15
                    ] = innermask[20] = "1"
            else:
                outermask[13] = "1"
            # Up
            if i >= cols:
                mask[i - cols] = "1"
                if i - cols == 12:
                    innermask[20] = innermask[21] = innermask[22] = innermask[
                        23
                    ] = innermask[24] = "1"
            else:
                outermask[7] = "1"
            # Down
            if i < len(self.__startbugs) - cols:
                mask[i + cols] = "1"
                if i + cols == 12:
                    innermask[0] = innermask[1] = innermask[2] = innermask[
                        3
                    ] = innermask[4] = "1"
            else:
                outermask[17] = "1"
            self.__neighbormasks[i] = {(0, "".join(mask))}
            if outermask.count("1") > 0:
                self.__neighbormasks[i].add((-1, "".join(outermask)))
            if innermask.count("1") > 0:
                self.__neighbormasks[i].add((1, "".join(innermask)))

    def get_p1(self) -> int:
        current = self.__startbugs
        seen = {current}
        while True:
            nextminute = ""
            for i, c in enumerate(current):
                for level, mask in self.__neighbormasks[i]:
                    if level != 0:
                        continue
                    neighbors = (int(mask, 2) & int(current, 2)).bit_count()
                    if (c == "1" and neighbors == 1) or (
                        c == "0" and 1 <= neighbors <= 2
                    ):
                        nextminute += "1"
                    else:
                        nextminute += "0"
            if nextminute not in seen:
                seen.add(nextminute)
            else:
                return int(nextminute[::-1], 2)
            current = nextminute

    def get_p2(self, minutes: int = 200) -> int:
        current = {0: self.__startbugs}
        empty = "0" * len(self.__startbugs)
        upper = lower = 0
        for _ in range(minutes):
            # Add outer levels in both directions if current outer is not empty
            if current[upper] != empty:
                upper += 1
                current[upper] = empty
            if current[lower] != empty:
                lower -= 1
                current[lower] = empty
            nextminute = {}

            for level, val in current.items():
                nextminute[level] = ""
                for i, c in enumerate(val):
                    if i == 12:
                        nextminute[level] += "0"
                        continue
                    neighbors = 0
                    for d_level, mask in self.__neighbormasks[i]:
                        if level + d_level in current:
                            neighbors += (
                                int(mask, 2) & int(current[level + d_level], 2)
                            ).bit_count()
                    if (c == "1" and neighbors == 1) or (
                        c == "0" and 1 <= neighbors <= 2
                    ):
                        nextminute[level] += "1"
                    else:
                        nextminute[level] += "0"
            current = nextminute
        return sum(level.count("1") for level in current.values())


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
