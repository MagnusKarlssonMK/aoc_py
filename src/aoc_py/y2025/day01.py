"""
2025 day 01 - Secret Entrance

Part 1

* Store the input as a vector of signed integer values.
* Then for all input values, use modulo operation to keep updating the dial value, but we need to
  use the rem_euclid function for correct result when the sum of the dial and the next value is negative.
* Increment counter whenever the dial value is zero.

Part 2

For all input values,
* If the input value is positive, increment the counter with (dial + input value) / 100, i.e.
  the number of times the dial will wrap around.
* Else if the dial is currently zero, increment the counter with the abs(input value) / 100. We
  need to handle this case separately to avoid counting the current zero dial value twice.
* Else, the input value is negative, so we need to "count backwards"; increment the counter
  with (100 - dial + abs(input value)) / 100.
* Then update the dial with the same modulo operation as in part 1.

A possible alternative solution for part 2 could be to keep track of the current direction instead of
working with signed integers, and flip the dial around whenever the direction changes. That way, all
changes to the dial will be in the positive direction, i.e. there would be no need to handle
"left" (negative) values separately.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__rotations = [
            int(line[1:]) if line[0] == "R" else -int(line[1:])
            for line in s.splitlines()
        ]

    def get_p1(self) -> int:
        zero_count = 0
        dial = 50
        for v in self.__rotations:
            dial = (dial + v) % 100
            if dial == 0:
                zero_count += 1
        return zero_count

    def get_p2(self) -> int:
        zero_count = 0
        dial = 50
        for v in self.__rotations:
            if v >= 0:
                zero_count += (dial + v) // 100
            elif dial == 0:
                zero_count += abs(v) // 100
            else:
                zero_count += (100 - dial + abs(v)) // 100
            dial = (dial + v) % 100
        return zero_count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
