"""
2023 day 13 - Point of Incidence
"""
def ismirror(patternlist: list[int], candidate: int, wildcard: bool) -> bool:
    """If wildcard == True, the wild card for part 2 has not yet been used."""
    if candidate >= (len(patternlist) - 1) or candidate < 0:
        return not wildcard
    elif patternlist[candidate] == patternlist[candidate + 1]:
        newlist = [item for z, item in enumerate(patternlist) if (z < candidate) or z > (candidate + 1)]
        return ismirror(newlist, candidate - 1, wildcard)
    elif wildcard and (patternlist[candidate] ^ patternlist[candidate + 1]).bit_count() == 1:#bin(patternlist[candidate] ^ patternlist[candidate + 1]).count("1") == 1:
            newlist = [item for z, item in enumerate(patternlist) if (z < candidate) or z > (candidate + 1)]
            return ismirror(newlist, candidate - 1, False)
    return False


def getmirrorscore(patternlist: list[int], wildcard: bool) -> int:
    for index in range(len(patternlist) - 1):
        if ismirror(patternlist, index, wildcard):
            return index + 1
    return 0


class Pattern:
    def __init__(self, rawstr: str) -> None:
        rows: list[str] = []
        self.__binrows: list[int] = []
        self.__bincolumns: list[int] = []
        # Convert input to a string of binary characters '0' and '1'
        for line in rawstr.splitlines():
            convertedstr = ''.join(['0' if c == '.' else '1' for c in line])
            rows.append(convertedstr)
            self.__binrows.append(int(convertedstr, 2))

        for i, _ in enumerate(rows[0]):
            convertedstr = ''.join([r[i] for r in rows])
            self.__bincolumns.append(int(convertedstr, 2))

    def getscore(self, wildcard: bool) -> int:
        retval = 0
        retval += 100 * getmirrorscore(self.__binrows, wildcard)
        retval += getmirrorscore(self.__bincolumns, wildcard)
        return retval


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__patterns = [Pattern(block) for block in rawstr.split('\n\n')]

    def get_totalscore(self, wildcard: bool = False) -> int:
        return sum([p.getscore(wildcard) for p in self.__patterns])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_totalscore())
        if part in (None, 2):
            p2 = str(p.get_totalscore(True))

        return p1, p2
