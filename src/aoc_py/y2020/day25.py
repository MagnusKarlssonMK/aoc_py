"""
2020 day 25 - Combo Breaker

The public keys are powers of the seed modulo the modulus. Find the card key's discrete log (its loop
size) with baby-step giant-step, then raise the door key to that power to get the encryption key.
"""

from math import isqrt

_MOD = 20201227
_SEED = 7


def discrete_log(target: int, base: int, mod: int) -> int:
    """Return x such that base ** x == target (mod mod), via baby-step giant-step."""
    n = isqrt(mod) + 1
    baby_steps: dict[int, int] = {}
    value = 1
    for power in range(n):
        _ = baby_steps.setdefault(value, power)
        value = value * base % mod
    factor = pow(base, -n, mod)
    gamma = target
    for giant_step in range(n):
        if gamma in baby_steps:
            return giant_step * n + baby_steps[gamma]
        gamma = gamma * factor % mod
    raise ValueError(f"No discrete log of {target} base {base} mod {mod}")


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__card_pub_key, self.__door_pub_key = list(map(int, rawstr.splitlines()))

    def get_p1(self) -> int:
        loop_size = discrete_log(self.__card_pub_key, _SEED, _MOD)
        return pow(self.__door_pub_key, loop_size, _MOD)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = "-"

    return p1, p2
