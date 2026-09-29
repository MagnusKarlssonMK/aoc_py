"""
2021 day 8 - Seven Segment Search

Part 1

Straightforward; parse the input data, then count the elements on the right side of the divider
with a length of 2, 3, 4 or 7 and add them up.

Part 2

A bit more complicated. Start with the left side, identify 1, 4, 7 and 8 by their unique lengths. The segment
mapping to 'a' can then be determined from the difference between 1 and 7. Then 3 can be identified by looking at
the signals with length 5, where 3 will be the only one containing the entire 7. With this, by looking at 4 now we
can determine the segment mapping to 'b' and 'd'. From here on we should have enough information to identify the
rest of the numbers and mappings.
Store the signals in sets to be able to use the '-' operator to find the difference between numbers.
"""

from typing import Final

SEGMENTS: Final[dict[int, str]] = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}

SEGMENTS_REV: Final[dict[frozenset[str], int]] = {
    frozenset(seg): nbr for nbr, seg in SEGMENTS.items()
}


class InputData:
    def __init__(self, s: str) -> None:
        self.__lines = [
            (row[0].split(), row[1].split())
            for row in [line.split(" | ") for line in s.splitlines()]
        ]

    def get_p1(self) -> int:
        p1 = 0
        for _, right in self.__lines:
            p1 += sum([1 for word in right if len(word) in (2, 3, 4, 7)])
        return p1

    def get_p2(self) -> int:
        return sum([self.__decode_line(line) for line in self.__lines])

    def __decode_line(self, line: tuple[list[str], list[str]]) -> int:
        """Decode one entry's output value from the wire mapping its ten patterns imply."""
        pattern, output = line
        numbers: dict[int, list[set[str]]] = {nbr: [] for nbr in range(10)}
        for p in pattern:  # Store candidate signals for each number based on length
            for nbr, seg in SEGMENTS.items():
                if len(p) == len(seg):
                    numbers[nbr].append(set(p))
        one, four, seven = numbers[1][0], numbers[4][0], numbers[7][0]
        # 3 is the only length 5 signal that holds all of 7
        numbers[3] = [sig for sig in numbers[3] if not seven - sig]
        three = numbers[3][0]
        mapping: dict[str, set[str]] = {
            "a": seven - one,  # Determine 'a' from 7 and 1
            "b": four - three,  # Determine 'b' from 4 and 3
        }
        # Determine 'd' from 4 and 1, less the 'b' already found
        mapping["d"] = four - one - mapping["b"]
        # of the two length 5 signals left, the one missing 'b' is 2 and the other is 5
        numbers[2] = [sig for sig in numbers[2] if sig != three and mapping["b"] - sig]
        numbers[5] = [
            sig for sig in numbers[5] if sig != three and not mapping["b"] - sig
        ]
        mapping["c"] = seven - numbers[5][0]  # Determine 'c' from 7 and 5
        mapping["e"] = numbers[2][0] - three  # Determine 'e' from 2 and 3
        mapping["f"] = seven - numbers[2][0]  # Determine 'f' from 7 and 2
        mapping["g"] = three - seven - mapping["d"]  # Determine 'g' from 3, 7 and 'd'

        # Invert the map and translate the output
        wires = {"".join(segs): nbr for nbr, segs in mapping.items()}
        return int(
            "".join(
                str(SEGMENTS_REV[frozenset(wires[wire] for wire in signal)])
                for signal in output
            )
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
