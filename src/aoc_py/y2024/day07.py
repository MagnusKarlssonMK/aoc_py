"""
2024 day 7 - Bridge Repair

Solves both parts in one go through a recursive function, which attempts to
fully validate each equation, and only resorts to use the concatenation
operation if it's the only way to succeed at the validation. The state of
whether or not concatenation has been used combined with the calculated value
is carried up through the recursion chain through the return value.
"""
from enum import Enum


class CalibrationResult(Enum):
    OK = 0,
    CONCATINATED_OK = 1,
    NOT_OK = 2


def concatinate(right: int) -> int:
    multiplier = 10
    while multiplier <= right:
        multiplier *= 10
    return multiplier


class Equation:
    def __init__(self, rawstr: str) -> None:
        tv, nbrs = rawstr.split(": ")
        self.__testvalue = int(tv)
        self.__numbers = [int(nbr) for nbr in nbrs.split()]

    def calibrate(self) -> tuple[CalibrationResult, int]:
        return self.__validate(self.__numbers[0], self.__numbers[1:])

    def __validate(self, total: int, nbrs: list[int]) -> tuple[CalibrationResult, int]:
        if len(nbrs) == 0:
            return (CalibrationResult.OK, total) if total == self.__testvalue else (CalibrationResult.NOT_OK, 0)
        elif total > self.__testvalue:
            return CalibrationResult.NOT_OK, 0
        else:
            add_result, add_value = self.__validate(total + nbrs[0], nbrs[1:])
            if add_result == CalibrationResult.OK:
                return add_result, add_value
            mul_result, mul_value = self.__validate(total * nbrs[0], nbrs[1:])
            if mul_result == CalibrationResult.OK:
                return mul_result, mul_value
            if add_result == CalibrationResult.CONCATINATED_OK:
                return add_result, add_value
            if mul_result == CalibrationResult.CONCATINATED_OK:
                return mul_result, mul_value
            conc_result, conc_value = self.__validate(total * concatinate(nbrs[0]) + nbrs[0], nbrs[1:])
            if conc_result != CalibrationResult.NOT_OK:
                return CalibrationResult.CONCATINATED_OK, conc_value
        return CalibrationResult.NOT_OK, 0


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__equations = [Equation(line) for line in rawstr.splitlines()]

    def get_calibration_result(self) -> tuple[int, int]:
        p1 = p2 = 0
        for e in self.__equations:
            r, v = e.calibrate()
            if r == CalibrationResult.OK:
                p1 += v
                p2 += v
            elif r == CalibrationResult.CONCATINATED_OK:
                p2 += v
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
        p1, p2 = "-1"
        p = InputData(inputdata)
        part1, part2 = p.get_calibration_result()
        if part in (None, 1):
            p1 = str(part1)
        if part in (None, 2):
            p2 = str(part2)

        return p1, p2
