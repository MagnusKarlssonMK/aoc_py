"""
2022 day 6 - Tuning Trouble
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__datastream = s

    def get_processed_characters(self, start_len: int = 4) -> int:
        for idx in range(len(self.__datastream) - (start_len - 1)):
            if len(set(self.__datastream[idx : idx + start_len])) == start_len:
                return idx + start_len
        return -1


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_processed_characters())
    if part in (None, 2):
        p2 = str(p.get_processed_characters(14))

    return p1, p2
