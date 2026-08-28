"""
2025 day 2 - Gift Shop

Part 1

For each range,
1) If the first number in the range is evenly divisible by 2, split it in two and take the first part (1234 -> 12).
   If not, start with the next number where it would increase the number of digits (e.g. 972 -> 1000).
2) Create a new candidate id by combining the number from 1) with itself (12 -> 1212).
3) If that candidate id is bigger than the second value in the range, stop.
4) If that candidate id is bigger than the first value in the range, an invalid value has been found; add it to the total.
5) Increment the candidate id (12 -> 13) and go back to 2).

## Part 2

Pretty much same as part 1, except,
* Instead of just splitting in 2 parts, loop over splits in different part sizes, from 2 up to the number of digits in
  the second value in the range.
* The same number can be found with different part lengths, but should only be counted once. So the identified invalid
  numbers are stored in a set and then summarized at the end to get rid of duplicates.
"""

import math
from typing import cast


def get_invalid(v1: str, v2: str) -> int:
    start_id = int(v1)
    stop_id = int(v2)
    nbrof_parts = 2

    invalid = 0
    d: int = len(v1) // nbrof_parts
    m: int = len(v1) % nbrof_parts
    next_part: int = (
        int(v1[0 : d])
        if m == 0
        else 10**d
    )

    while True:
        nbrof_part_digits: int = int(1 + int(math.log10(abs(next_part))))
        # Using cast as temporary fix for basedpyright issue with pow
        p = cast(int, 10**nbrof_part_digits)
        candidate_id: int = next_part + (next_part * p)
        if candidate_id > stop_id:
            break
        if candidate_id >= start_id:
            invalid += candidate_id
        next_part += 1

    return invalid

def get_multiple_invalid(v1: str, v2: str) -> int:
    start_id = int(v1)
    stop_id = int(v2)
    nbrof_parts = 2
    invalid: set[int] = set()

    while nbrof_parts <= len(v2):
        d: int = len(v1) // nbrof_parts
        m: int = len(v1) % nbrof_parts
        next_part = (
            int(v1[0 : d])
            if m == 0
            else 10**d
        )

        while True:
            nbrof_part_digits = 1 + int(math.log10(abs(next_part)))
            candidate_id = sum(
                [
                    next_part * 10**(p * nbrof_part_digits)
                    for p in range(nbrof_parts)
                ]
            )
            if candidate_id > stop_id:
                break
            if candidate_id >= start_id:
                invalid.add(candidate_id)
            next_part += 1
        nbrof_parts += 1

    return sum(invalid)


class InputData:
    def __init__(self, s: str) -> None:
        self.__rotations = [
            (v[0], v[1]) for v in [r.split("-", 1) for r in s.split(",")]
        ]

    def get_p1(self) -> int:
        return sum([get_invalid(v1, v2) for (v1, v2) in self.__rotations])

    def get_p2(self) -> int:
        return sum([get_multiple_invalid(v1, v2) for (v1, v2) in self.__rotations])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
