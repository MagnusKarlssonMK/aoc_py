"""
2018 day 5 - Alchemical Reduction

Mainly (ab)using the ord() function to compare characters while generating reacted values or removing units.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__polymer = s
        self.__offset = ord("a") - ord("A")

    def __get_reacted_unit_count(self, polymer: str) -> int:
        i = 0
        poly = list(polymer)
        while i < len(poly) - 1:
            if abs(ord(poly[i]) - ord(poly[i + 1])) == self.__offset:
                del poly[i : i + 2]
                if i > 0:
                    i -= 1
            else:
                i += 1
        return len(poly)

    def __delete_unit(self, unit: int) -> str:
        u = unit, unit + self.__offset
        return "".join(c for c in self.__polymer if ord(c) not in u)

    def get_p1(self) -> int:
        return self.__get_reacted_unit_count(self.__polymer)

    def get_p2(self) -> int:
        shortest = None
        for c in range(ord("A"), ord("Z") + 1):
            removed_len = self.__get_reacted_unit_count(self.__delete_unit(c))
            if not shortest or removed_len < shortest:
                shortest = removed_len
        return shortest if shortest else -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
