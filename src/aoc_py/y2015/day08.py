"""
2015 day 8 - Matchsticks

Every line of the input is one string literal. Both parts ask how much a line is inflated by having been written down.

Part 1

The gap between code and memory. A line's code count is its length as written, delimiters included, while its memory
count is the length of the value once decoded, so the surrounding pair of quotes is always worth 2. Each escape saves
the difference between its own length and the single character it stands for: a two character escape, a backslash before
a quote or before another backslash, saves 1, while the four character hexadecimal form saves 3. Adding 2 per line and
then 1 or 3 per escape therefore reaches the same total as subtracting the decoded length outright, without having to
decode anything.

Part 2

How much longer each line becomes when it is escaped a second time, which is 2 for a fresh pair of delimiters plus 1 for
every quote and every backslash the line already holds. Note this measures the line as written rather than the decoded
value, so the original delimiters are escaped along with everything else; escaping the decoded value instead gives a
different and considerably smaller total.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__literals = s.splitlines()

    def get_p1(self) -> int:
        count = 0
        for line in self.__literals:
            count += 2  # Add 2 for the surrounding double quotes
            i = 1
            while i < len(line) - 1:
                if line[i] == "\\":
                    if line[i + 1] in ('"', "\\"):
                        count += 1
                        i += 1
                    elif line[i + 1] == "x":
                        count += 3
                        i += 3
                    else:
                        # The puzzle promises no other escape ever appears, but should one turn up it then treat it
                        # as a single character, so it saves one. Whatever follows the backslash is ordinary text.
                        count += 1
                i += 1
        return count

    def get_p2(self) -> int:
        count = 0
        for line in self.__literals:
            count += 2  # Surrounding double quotes will expand by one character each
            for c in line:
                if c in ('"', "\\"):
                    count += 1
        return count


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
