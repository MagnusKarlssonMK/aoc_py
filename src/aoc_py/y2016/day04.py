"""
2016 day 4 - Security Through Obscurity

Each room line holds dash separated words, a sector id, and a checksum in brackets. The room is real when the
checksum is the five letters occurring most often in its name, ties broken alphabetically, so part 1 sums the
sector ids of the real rooms. Part 2 shifts every letter of the name forward by the sector id and looks for the
room that decodes to northpole object storage; only a real room may answer, and when nothing matches the answer
is -1 rather than some plausible looking sector id.
"""


class Room:
    def __init__(self, s: str) -> None:
        self.__sector_id = 0
        self.__checksum = ""
        left, self.__checksum = s.rstrip("]").split("[")
        parts = left.split("-")
        words = parts[0:-1]
        self.__sector_id = int(parts[-1])
        self.__words = tuple(words)

    def validate(self) -> int:
        """Generates the checksum for the words, and returns the sector id if it
        matches the stored checksum from the input, otherwise zero."""
        letters = "".join(self.__words)
        lettercount: dict[str, int] = {}
        for c in letters:
            if c not in lettercount:
                lettercount[c] = 1
            else:
                lettercount[c] += 1
        if len(lettercount) >= len(self.__checksum):
            # Sort by number of occurrences first, alphabetically second, and extract the top 5
            candidate = "".join(
                [
                    i[0]
                    for i in sorted(lettercount.items(), key=lambda x: (-x[1], x[0]))[
                        : len(self.__checksum)
                    ]
                ]
            )
            if candidate == self.__checksum:
                return self.__sector_id
        return 0

    def decode_check(self, target: list[str]) -> bool:
        """Returns whether the decoded name of the room matches the target."""
        # 1. Check number of words
        if len(self.__words) != len(target):
            return False
        # 2. Check number of letters in each word
        for left, right in zip(self.__words, target):
            if len(left) != len(right):
                return False
        # 3. Decode the words and compare to target
        decoded_name = [
            "".join(
                [
                    chr(
                        (ord(c) - ord("a") + self.__sector_id)
                        % (1 + ord("z") - ord("a"))
                        + ord("a")
                    )
                    for c in word
                ]
            )
            for word in self.__words
        ]
        return decoded_name == target


class InputData:
    def __init__(self, s: str) -> None:
        self.__rooms: list[Room] = [Room(line) for line in s.splitlines()]

    def solve(self) -> tuple[int, int]:
        p1 = 0
        p2 = -1
        TARGET = ["northpole", "object", "storage"]
        for room in self.__rooms:
            s_id = room.validate()
            p1 += s_id
            if s_id and room.decode_check(TARGET):
                p2 = s_id
        return p1, p2


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.solve()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
