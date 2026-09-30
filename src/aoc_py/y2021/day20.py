"""
2021 day 20 - Trench Map

Converts the image to rows of integer values based on binary representation of '#' and '.', and then performs the
enhancement steps through bitmasking / bitshifting. Adds an extra layer in the map for every step.
Possibly this could be further optimized by pruning the boundaries in case the lit pixels stops growing outwards at
some point.
Also - unlike the example input, the real input toggles the void at each enhancement. So we also need to keep track
of the state of the void and use that for creating the outer buffer to get the correct result at the boundaries. The
void can only start alternating once the first algorithm entry is lit, since until then the lookup keeps reading
that same first entry; for the example input it is dark, so its void stays dark for every step.
"""

from typing import Final

P1_NBR_STEPS: Final = 2
P2_NBR_STEPS: Final = 50


class InputData:
    def __init__(self, rawstr: str) -> None:
        algo, img_input = rawstr.split("\n\n")
        self.__voidvalue = "0"
        self.__algorithm = ["1" if c == "#" else "0" for c in algo]
        self.__x_range = 0
        self.__image = [0, 0]
        for line in img_input.splitlines():
            self.__x_range = len(line) + 4
            self.__image.append(
                int("".join(["1" if c == "#" else "0" for c in line]) + "00", 2)
            )
        self.__image.append(0)
        self.__image.append(0)
        self.__initialimage = list(self.__image)
        self.__initialxrange = self.__x_range
        self.__y_range = len(self.__image)

    def __enhance_image(self) -> None:
        self.__voidvalue = self.__algorithm[0 if self.__voidvalue == "0" else -1]
        voidrow = (
            0
            if self.__voidvalue == "0"
            else int("".join(["1" for _ in range(self.__x_range + 2)]), 2)
        )
        new_image = [voidrow, voidrow]
        # Note: first and last row, and leftmost and rightmost columns just need to be there for the next positions
        # to draw from, but it's easier to just recreate them every round while also adding an extra new layer, rather
        # than converting based on void value. Thus adding buffer rows / cols twice every time.
        for y in range(1, self.__y_range - 1):
            new_row = self.__voidvalue + self.__voidvalue
            for x in range(1, self.__x_range - 1):
                v = (
                    (((self.__image[y - 1] >> (self.__x_range - x - 2)) & 7) << 6)
                    + (((self.__image[y] >> (self.__x_range - x - 2)) & 7) << 3)
                    + ((self.__image[y + 1] >> (self.__x_range - x - 2)) & 7)
                )
                new_row += self.__algorithm[v]
            new_row += self.__voidvalue + self.__voidvalue
            new_image.append(int(new_row, 2))
        new_image.append(voidrow)
        new_image.append(voidrow)
        self.__image = new_image
        self.__x_range += 2
        self.__y_range += 2

    def __lit_pixels(self) -> int:
        return sum([line.bit_count() for line in self.__image])

    def run_steps(self) -> tuple[int, int]:
        """Reports the number of lit pixels after Part 1's and Part 2's number of enhancement
        steps. The image and the void are restored to their initial state first, so the
        enhancement can be run more than once."""
        self.__image = list(self.__initialimage)
        self.__x_range = self.__initialxrange
        self.__y_range = len(self.__image)
        self.__voidvalue = "0"
        p1 = 0
        for step in range(P2_NBR_STEPS):
            self.__enhance_image()
            if step == P1_NBR_STEPS - 1:
                p1 = self.__lit_pixels()
        return p1, self.__lit_pixels()


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    r1, r2 = InputData(inputdata).run_steps()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
