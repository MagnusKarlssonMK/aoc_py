"""
2016 day 6 - Signals and Noise

Pretty much just walk through the codes and store the character count in a dictionary for each position. This can then
be sorted (increasing or decreasing depending on part 1 or 2) to generate the result.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__codes = s.splitlines()

    def decode_signal(self) -> tuple[str, str]:
        counter: list[dict[str, int]] = [{} for _, _ in enumerate(self.__codes[0])]
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
