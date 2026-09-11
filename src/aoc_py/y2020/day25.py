"""
2020 day 25 - Combo Breaker

Step 1: Determine the loop size from the public card key
Step 2: Use the loop size to transform the public door key into the encryption key
"""


class InputData:
    __MOD = 20201227
    __SEED = 7

    def __init__(self, rawstr: str) -> None:
        self.__card_pub_key, self.__door_pub_key = list(map(int, rawstr.splitlines()))

    def get_p1(self) -> int:
        # Get the loop size
        loop_size = 0
        value = 1
        while self.__card_pub_key != value:
            loop_size += 1
            value = (InputData.__SEED * value) % InputData.__MOD
        # Get the key from transforming the door key
        value = 1
        for _ in range(loop_size):
            value = (self.__door_pub_key * value) % InputData.__MOD
        return value


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
