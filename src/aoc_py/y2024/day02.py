"""
2024 day 2 - Red-Nosed Reports
"""

from enum import Enum
from itertools import pairwise


class SafetyLevels(Enum):
    SAFE = 1
    DAMPENER_SAFE = 2
    UNSAFE = 3


class Report:
    def __init__(self, line: str) -> None:
        self.__levels = [int(c) for c in line.split()]

    def get_safety_level(self) -> SafetyLevels:
        def is_safe(levels: list[int]) -> bool:
            diffs = [(abs(j - i), 1 if j - i > 0 else -1) for i, j in pairwise(levels)]
            return all(1 <= v <= 3 and o == diffs[0][1] for v, o in diffs)

        if is_safe(self.__levels):
            return SafetyLevels.SAFE
        else:
            for n, _ in enumerate(self.__levels):
                if is_safe(self.__levels[0:n] + self.__levels[n + 1 :]):
                    return SafetyLevels.DAMPENER_SAFE
        return SafetyLevels.UNSAFE


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__reports = [Report(line) for line in rawstr.splitlines()]

    def get_safe_reports(self) -> tuple[int, int]:
        safety = [r.get_safety_level() for r in self.__reports]
        safe = safety.count(SafetyLevels.SAFE)
        almost_safe = safety.count(SafetyLevels.DAMPENER_SAFE)
        return safe, safe + almost_safe


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    part1, part2 = p.get_safe_reports()
    if part in (None, 1):
        p1 = str(part1)
    if part in (None, 2):
        p2 = str(part2)

    return p1, p2
