"""
2015 day 10 - Elves Look, Elves Say

Walk the sequence once per round, counting each run of equal digits and emitting the count followed by the digit. Only
the length of the result is ever asked for, but the sequence itself has to be built each round, since the next one
reads it.

Part 1 runs 40 rounds and part 2 runs 50, so the two answers come from two separate walks and the first 40 rounds are
discarded before the second begins. That redundancy is the only obvious saving left, and it is under a tenth of the
runtime.

The plain build is already close to the best available. Grouping the runs with itertools.groupby is about three times
slower, because summing each group costs more than the inline comparison it replaces. Collecting the pieces and joining
them is around a tenth faster. Carrying a run-length representation instead of the string avoids materialising the seven
megabyte result but is both slower and far heavier on memory, since a list of tuples costs much more per element than a
single character does.
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
