"""
2019 day 8 - Space Image Format

Store each layer as an array of numbers, don't convert it to 2D until building the actual image. For solving
part 1, having it as simple lists is easier.
"""

from collections import Counter


class InputData:
    def __init__(self, s: str, width: int = 25, height: int = 6) -> None:
        self.__width = width
        self.__height = height
        self.__layers: list[list[int]] = []
        i = 0
        while i < len(s):
            self.__layers.append(
                [int(c) for c in s[i : i + self.__height * self.__width]]
            )
            i += self.__width * self.__height

    def get_p1(self) -> int:
        results: list[tuple[int, int]] = []
        for layer in self.__layers:
            c = Counter(layer)
            results.append((c[0], c[1] * c[2]))
        results.sort(key=lambda x: x[0])
        return results[0][1]

    def get_p2(self) -> str:
        img = self.__layers[0]
        for layeridx in range(1, len(self.__layers)):
            for i, nbr in enumerate(self.__layers[layeridx]):
                if img[i] == 2:
                    img[i] = nbr
        result = ""
        for i, n in enumerate(img):
            if i % self.__width == 0:
                result += "\n"
            result += "#" if n == 1 else " "
        return result


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
