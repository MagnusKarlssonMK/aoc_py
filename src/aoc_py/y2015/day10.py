"""
2015 day 10 - Elves Look, Elves Say

Pretty much just walk through the string and generate the new number, so basically brute-force. Part 1 is decently
fast but part 2 takes a couple of seconds. Might need to investigate further in the future if there are more clever
ways to approach this.
"""


class InputData:
    def __init__(self, s: str) -> None:
        self.__startnbrs = s

    def get_generated_length(self, rounds: int) -> int:
        sequence = self.__startnbrs
        for _ in range(rounds):
            new_seq = ""
            count = 0
            currentchar = ""
            for c in sequence:
                if c == currentchar:
                    count += 1
                else:
                    if count > 0:
                        new_seq += str(count) + currentchar
                    count = 1
                    currentchar = c
            if count > 0:
                new_seq += str(count) + currentchar
            sequence = new_seq
        return len(sequence)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_generated_length(40))
    if part in (None, 2):
        p2 = str(p.get_generated_length(50))

    return p1, p2
