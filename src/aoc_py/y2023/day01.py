"""
2023 day 1 - Trebuchet?!

For part 1, simply extract all numbers from the string and combine the first and last digit.
For part 2, first pre-process the string by replacing spelled out digits with the same word but with the actual digit
inserted in the middle, in a place where it won't destroy the string in case numbers are overlapping (e.g. 'threeight').
"""
class Calibrationstring:
    def __init__(self, inputstr: str) -> None:
        self.__calstring = inputstr

    def getcalibrationvalue(self, spelled_out: bool) -> int:
        digits = {'one': 'o1ne', 'two': 't2wo', 'three': 'th3ree', 'four': 'fo4ur', 'five': 'fi5ve',
                  'six': 'si6x', 'seven': 'se7ven', 'eight': 'eig8th', 'nine': 'ni9ne'}
        strcopy = self.__calstring
        if spelled_out:
            for olddigit, newname in digits.items():
                strcopy = strcopy.replace(olddigit, newname)
        digits = [char for char in strcopy if char.isdigit()]
        return 0 if len(digits) == 0 else int(digits[0] + digits[-1])


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__values = [Calibrationstring(line) for line in rawstr.splitlines()]

    def get_calibration_sum(self, spelled_out: bool = False) -> int:
        return sum([v.getcalibrationvalue(spelled_out) for v in self.__values])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        if part in (None, 1):
            p1 = str(p.get_calibration_sum())
        if part in (None, 2):
            p2 = str(p.get_calibration_sum(True))

        return p1, p2
