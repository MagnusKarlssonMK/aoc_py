"""
2024 day 7 - Bridge Repair

Each equation is solved backwards from its test value by inverting the last operation
applied to the final term: '+' becomes a subtraction, '*' is only possible when the
test value is divisible by the term, and '||' is only possible when the test value
ends with the digits of the term. Searching without concatenation first decides part 1;
if that fails, searching with concatenation decides part 2.
"""


class Equation:
    def __init__(self, rawstr: str) -> None:
        tv, nbrs = rawstr.split(": ")
        self.__testvalue = int(tv)
        self.__numbers = [int(nbr) for nbr in nbrs.split()]
        self.__number_strings = [str(nbr) for nbr in self.__numbers]

    def calibrate(self) -> tuple[int, int]:
        """Returns the calibration level (1 = solvable without concatenation,
        2 = only solvable with concatenation, 0 = unsolvable) and the test value."""
        if self.__solve(len(self.__numbers) - 1, self.__testvalue, False):
            return 1, self.__testvalue
        if self.__solve(len(self.__numbers) - 1, self.__testvalue, True):
            return 2, self.__testvalue
        return 0, 0

    def __solve(self, index: int, target: int, allow_concat: bool) -> bool:
        """Checks if the first index+1 numbers can be combined (left to right) into target."""
        if index == 0:
            return self.__numbers[0] == target
        nbr = self.__numbers[index]
        if target > nbr and self.__solve(index - 1, target - nbr, allow_concat):
            return True
        if target % nbr == 0 and self.__solve(index - 1, target // nbr, allow_concat):
            return True
        if allow_concat:
            target_str, nbr_str = str(target), self.__number_strings[index]
            if (
                len(target_str) > len(nbr_str)
                and target_str.endswith(nbr_str)
                and self.__solve(
                    index - 1, int(target_str[: -len(nbr_str)]), allow_concat
                )
            ):
                return True
        return False


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__equations = [Equation(line) for line in rawstr.splitlines()]

    def get_calibration_result(self) -> tuple[int, int]:
        p1 = p2 = 0
        for e in self.__equations:
            level, value = e.calibrate()
            if level == 1:
                p1 += value
                p2 += value
            elif level == 2:
                p2 += value
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    part1, part2 = p.get_calibration_result()
    if part in (None, 1):
        p1 = str(part1)
    if part in (None, 2):
        p2 = str(part2)

    return p1, p2
