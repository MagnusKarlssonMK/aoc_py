"""
2023 day 1 - Trebuchet?!

For part 1, simply extract all numbers from the string and combine the first and last digit.
For part 2, first pre-process the string by replacing spelled out digits with the same word but with the actual digit
inserted after its first letter, in a place where it won't destroy the string in case numbers are overlapping
(e.g. 'threeight'). A spelled out word also counts when it genuinely is one, so 'zoneight' holds both 'one' and
'eight' and the calibration value of that line is 14.
"""

from typing import Final

# Every replacement keeps the rest of the word intact, so overlapping words survive in insertion order:
# 'threeight' -> 'th3reeight' -> 'th3reeig8th'.
SPELLED_DIGITS: Final = {
    "one": "o1ne",
    "two": "t2wo",
    "three": "th3ree",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6x",
    "seven": "se7ven",
    "eight": "eig8th",
    "nine": "ni9ne",
}


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__lines = rawstr.splitlines()

    def __calibration_sum(self, spelled_out: bool) -> int:
        total = 0
        for line in self.__lines:
            if spelled_out:
                for word, spelled in SPELLED_DIGITS.items():
                    line = line.replace(word, spelled)
            digits = [c for c in line if c.isdigit()]
            total += int(digits[0] + digits[-1]) if digits else 0
        return total

    def get_p1(self) -> int:
        return self.__calibration_sum(False)

    def get_p2(self) -> int:
        return self.__calibration_sum(True)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
