"""
2021 day 24 - Arithmetic Logic Unit

The instructions are a bit of a bait to implement an emulator, but that isn't actually very helpful. Instead, we need
to reverse engineer what the program is doing. The monad program consists of 14 identical chunks
of instructions with slightly different numbers as arguments, i.e. each chunk represents one calculation per digit in
the model number.

Following what a chunk does to z reduces the whole program to a stack. Each chunk zeroes x and y again on its way
through, so the only thing carried from one chunk to the next is z, and a chunk leaves it as one of z unchanged,
z // 26, or 26 * (z // 26) + digit + offset. A chunk that divides z by 1 leaves the stack where it is and, when
its check fails, pushes the digit onto it. A chunk that divides z by 26 instead pops a digit back off, or swaps the
top digit for a new one when the check fails. The goal is a z of zero at the end, so every digit pushed has to be
popped again, and each push is undone by the first pop after it, which makes the pairing a plain stack. The digit
that comes back off has to be the digit that went on, moved by the two chunks' numbers, and that pins both of them
at once.

Two things about a real input make that pairing the whole answer. Every chunk that divides z by 1 has an `add x` of
more than 9, so with a digit of at most 9 its check can never pass and it always pushes, which leaves only the
popping chunks to solve for. And the offset within a pair is small enough that both of its digits can be held
between 1 and 9, with one of them pinned against an end of that range.
"""

from dataclasses import dataclass
from typing import Final

MIN_DIGIT: Final = 1
MAX_DIGIT: Final = 9
# a chunk dividing z by this pushes a digit rather than popping one
PUSH_DIVISOR: Final = 1

# A chunk is always the same 18 instructions, and only three of them carry a number that varies
# from chunk to chunk. The rest either repeat a constant or just shuffle a register, so the layout
# can be indexed rather than searched.
DIV_Z_LINE: Final = 4  # div z 1 pushes a digit, div z 26 pops one back off
ADD_X_LINE: Final = 5  # add x N, the offset a popping chunk has to match
ADD_Y_LINE: Final = 15  # add y N, what a pushing chunk stores on the stack


@dataclass(frozen=True)
class Chunk:
    """One block of the program, cut down to the only two things the answer depends on: whether it
    pushes or pops, and the number it works with. What a pushing chunk works with is what it stores on
    the stack, and what a popping chunk works with is the offset the digit it pops has to match. The
    other number in each chunk is never read.
    """

    pushes: bool
    val: int


class InputData:
    def __init__(self, rawstr: str) -> None:
        blocks: list[list[list[str]]] = []
        for line in rawstr.splitlines():
            instr = line.split()
            if not instr:
                continue
            if instr[0] == "inp":
                blocks.append([instr])
            else:
                blocks[-1].append(instr)
        self.__chunks: list[Chunk] = []
        for block in blocks:
            pushes = int(block[DIV_Z_LINE][2]) == PUSH_DIVISOR
            line = ADD_Y_LINE if pushes else ADD_X_LINE
            self.__chunks.append(Chunk(pushes, int(block[line][2])))

    def get_answers(self) -> tuple[int, int]:
        """The largest and then the smallest model number the program accepts. Pairing up the
        chunks fixes the relation between the two digits of each pair, and only leaves the choice of
        how high along the 1-to-9 range to sit them, which puts one of the two against an end: the
        later digit for the largest number and the earlier one for the smallest. A well-formed
        program pairs off every push, since a push with no pop to undo it would leave z non-zero.
        """
        biggest = [MAX_DIGIT] * len(self.__chunks)
        smallest = [MIN_DIGIT] * len(self.__chunks)
        # (chunk, what it pushed), for the pushes that have not been undone yet
        pending: list[tuple[int, int]] = []
        for i, chunk in enumerate(self.__chunks):
            if chunk.pushes:
                pending.append((i, chunk.val))
                continue
            j, pushed = pending.pop()
            # the popped digit is the pushed one moved by this much
            delta = pushed + chunk.val
            biggest[j] = MAX_DIGIT - max(0, delta)
            biggest[i] = MAX_DIGIT + min(0, delta)
            smallest[j] = MIN_DIGIT - min(0, delta)
            smallest[i] = MIN_DIGIT + max(0, delta)
        return (int("".join(map(str, biggest))), int("".join(map(str, smallest))))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).get_answers()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
