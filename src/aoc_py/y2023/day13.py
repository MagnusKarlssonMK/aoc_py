"""
2023 day 13 - Point of Incidence

Each row of a pattern is converted to a single integer, and the same is done for the columns, so that a mirror
line only has to compare two integers for equality. The mirror line has to fall between two rows, which is why
the search runs from the first row up to the second to last one. For part 2, where exactly one cell is smudged,
the two rows beside the candidate line are xored and the line is only accepted when the two differ in a single
bit, since that bit is the smudge and it is the only one allowed.
"""


def is_mirror(patternlist: list[int], candidate: int, wildcard: bool) -> bool:
    """Returns whether the pattern is mirrored around a line just above row candidate, allowing one
    smudged cell when wildcard is True and the smudge has not been used yet."""
    if candidate >= (len(patternlist) - 1) or candidate < 0:
        return not wildcard
    left = patternlist[candidate]
    right = patternlist[candidate + 1]
    if left == right:
        next_wildcard = wildcard
    elif wildcard and (left ^ right).bit_count() == 1:
        next_wildcard = False
    else:
        return False
    newlist = [
        item for z, item in enumerate(patternlist) if z < candidate or z > candidate + 1
    ]
    return is_mirror(newlist, candidate - 1, next_wildcard)


def get_mirror_score(patternlist: list[int], wildcard: bool) -> int:
    for index in range(len(patternlist) - 1):
        if is_mirror(patternlist, index, wildcard):
            return index + 1
    return 0


class Pattern:
    def __init__(self, rawstr: str) -> None:
        rows = [
            "".join(["0" if c == "." else "1" for c in line])
            for line in rawstr.splitlines()
        ]
        self.__binrows = [int(row, 2) for row in rows]
        self.__bincolumns = [int("".join(col), 2) for col in zip(*rows)]

    def getscore(self, wildcard: bool) -> int:
        return 100 * get_mirror_score(self.__binrows, wildcard) + get_mirror_score(
            self.__bincolumns, wildcard
        )


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__patterns = [Pattern(block) for block in rawstr.split("\n\n")]

    def get_totalscore(self, wildcard: bool = False) -> int:
        return sum([p.getscore(wildcard) for p in self.__patterns])

    def get_p1(self) -> int:
        return self.get_totalscore()

    def get_p2(self) -> int:
        return self.get_totalscore(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
