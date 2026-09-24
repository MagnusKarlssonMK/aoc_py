"""
2017 day 21 - Fractal Art

Parts 1 & 2 are basically the same, Part 2 is pretty much just a stress test to see if the solution scales well with
larger numbers.
Takes the input and expands it into a dictionary of all possible combinations of 2- and 3-sized input blocks, and from
there it's mostly down to doing the necessary transformations for each step.
For a rainy day: a bit curious if it could run even faster by using recursion instead and expanding the dictionary
sort of like a memo cache along the way for larger block sizes?
"""

from typing import Final


def flipblock(inblock: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(["".join(reversed(b)) for b in inblock])


def rotateblock(inblock: tuple[str, ...]) -> tuple[str, ...]:
    return tuple(
        [
            "".join([inblock[row][col] for row in range(len(inblock))])
            for col in reversed(range(len(inblock)))
        ]
    )


class InputData:
    __START_IMAGE: Final = (".#.", "..#", "###")

    def __init__(self, rawstr: str) -> None:
        self.__transforms: dict[tuple[str, ...], tuple[str, ...]] = {}
        for line in rawstr.splitlines():
            left, right = line.split(" => ")
            inp1 = tuple(
                left.split("/")
            )  # Work with tuples to make it hashable and possible to use as dict key
            # Pre-compute the possible permutations of the left side
            inp2 = flipblock(inp1)
            out = tuple(right.split("/"))
            self.__transforms[inp1] = out
            self.__transforms[inp2] = out
            for _ in range(3):
                inp1 = rotateblock(inp1)
                inp2 = rotateblock(inp2)
                self.__transforms[inp1] = out
                self.__transforms[inp2] = out

    def get_pixel_count(self, iterations: int) -> int:
        image = list(InputData.__START_IMAGE)
        for _ in range(iterations):
            new_image: list[str] = []
            stepsize = 2 if len(image) % 2 == 0 else 3
            for row in range(0, len(image), stepsize):
                for _ in range(stepsize + 1):
                    new_image.append("")
                for col in range(0, len(image), stepsize):
                    block = [
                        image[row + i][col : col + stepsize] for i in range(stepsize)
                    ]
                    transformed_block = self.__transforms[tuple(block)]
                    target_row = (row // stepsize) * (stepsize + 1)
                    for i in range(stepsize + 1):
                        new_image[target_row + i] += transformed_block[i]
            image = new_image
        return "".join(image).count("#")


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_pixel_count(5))
    if part in (None, 2):
        p2 = str(p.get_pixel_count(18))

    return p1, p2
