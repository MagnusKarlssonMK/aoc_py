"""
2021 day 3 - Binary Diagnostic

Stores input values as binary values together with the bit width. Then for part 1 it's simply a
matter of calculating the gamma and epsilon ratings for all those values and multiplying them to
get the result. For part 2, the lists of values to consider need to be filtered down according to
the gamma and epsilon ratings one bit at a time, starting at the most significant bit. The answer
is then given by the final remaining number for the oxygen (gamma based) and scrubber (epsilon
based) ratings.
"""


def most_common_bit_is_one(numbers: list[int], mask: int) -> bool:
    """Returns whether the most common bit at `mask` is 1; ties resolve to 1 (gamma wins)."""
    ones = len([n for n in numbers if n & mask != 0])
    return 2 * ones >= len(numbers)


class InputData:
    def __init__(self, s: str) -> None:
        nbrs = s.splitlines()
        self.__numbers = [int(n, 2) for n in nbrs]
        self.__nbrbits = len(nbrs[0])

    def get_p1(self) -> int:
        gamma = 0
        epsilon = 0
        for mask in [1 << bit for bit in range(self.__nbrbits)]:
            if most_common_bit_is_one(self.__numbers, mask):
                gamma |= mask
            else:
                epsilon |= mask
        return gamma * epsilon

    def get_p2(self) -> int:
        oxygen_candidates = self.__numbers.copy()
        scrubber_candidates = self.__numbers.copy()

        for mask in [1 << bit for bit in reversed(range(self.__nbrbits))]:
            if len(oxygen_candidates) > 1:
                gamma_bit_is_one = most_common_bit_is_one(oxygen_candidates, mask)
                oxygen_candidates = [
                    c for c in oxygen_candidates if (c & mask != 0) == gamma_bit_is_one
                ]
            if len(scrubber_candidates) > 1:
                epsilon_bit_is_one = not most_common_bit_is_one(
                    scrubber_candidates, mask
                )
                scrubber_candidates = [
                    c
                    for c in scrubber_candidates
                    if (c & mask != 0) == epsilon_bit_is_one
                ]
        return (
            -1
            if len(oxygen_candidates) != 1 or len(scrubber_candidates) != 1
            else oxygen_candidates[0] * scrubber_candidates[0]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
