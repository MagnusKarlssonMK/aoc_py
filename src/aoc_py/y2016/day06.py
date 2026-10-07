"""
2016 day 6 - Signals and Noise

Count the characters of every column into a dict of dicts, then pick each column's winner with max (part 1) or min
(part 2) over the character counts. Dicts keep insertion order and max/min return the first extremal item, so a
tie goes to whichever character appeared first in that column.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__codes = s.splitlines()

    def decode_signal(self) -> tuple[str, str]:
        counter: list[dict[str, int]] = [{} for _ in self.__codes[0]]
        for code in self.__codes:
            for i, c in enumerate(code):
                if c not in counter[i]:
                    counter[i][c] = 1
                else:
                    counter[i][c] += 1
        signal = ""
        modified_signal = ""
        for cnt in counter:
            signal += max(cnt.items(), key=lambda x: x[1])[0]
            modified_signal += min(cnt.items(), key=lambda x: x[1])[0]
        return signal, modified_signal


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.decode_signal()
    if part in (None, 1):
        p1 = r1
    if part in (None, 2):
        p2 = r2

    return p1, p2
