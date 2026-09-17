"""
2015 day 19 - Medicine for Rudolph
"""


def match_indices(s: str, needle: str) -> list[int]:
    return [i for i in range(len(s) - len(needle) + 1) if s.startswith(needle, i)]


class InputData:
    __replacements: dict[str, list[str]]
    __molecule: str

    def __init__(self, s: str) -> None:
        r, self.__molecule = s.split("\n\n")
        self.__replacements = {}
        for line in r.splitlines():
            left, right = line.split(" => ")
            self.__replacements.setdefault(left, []).append(right)

    def get_p1(self) -> int:
        altered = set()
        for replaced, v in self.__replacements.items():
            for replacement in v:
                for i in match_indices(self.__molecule, replaced):
                    j = i + len(replaced)
                    altered.add(self.__molecule[:i] + replacement + self.__molecule[j:])
        return len(altered)

    def get_p2(self) -> int:
        elements = len([c for c in self.__molecule if c.isupper()])
        rn = self.__molecule.count("Rn")
        ar = self.__molecule.count("Ar")
        y = self.__molecule.count("Y")
        return elements - ar - rn - (2 * y) - 1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
