"""
2025 day 10 - Factory

Each machine is stored with bitmasks, so a button press is just an XOR. For every machine a
solution map is precomputed: each combination of button presses (press each at most once, since
pressing twice cancels) mapped to the mask it produces.

Part 1

Look the target light diagram up in the solution map and keep the solution with the fewest
button presses (fewest set bits).

Part 2

Recursively "bifurcate": the parity of the current joltage values must equal a mask reachable by
some button combination, so press that combination, subtract one from every affected (non zero)
value, halve everything and recurse. The solution map is reused to find parity matches without
recomputing them.
"""

from collections import deque


class Machine:
    def __init__(self, rawstr: str) -> None:
        lights, rest = rawstr.split(" ", 1)
        buttons, joltage = rest.rsplit(" ", 1)
        self.__light_diagram: int = sum(
            1 << i for i, c in enumerate(lights.strip("[]")) if c == "#"
        )
        self.__buttons: list[int] = [
            sum(1 << int(n) for n in part.strip("()").split(","))
            for part in buttons.split()
        ]
        self.__joltage: list[int] = [int(n) for n in joltage.strip("{}").split(",")]

        # Enumerate every button combination once by only ever adding a button beyond the highest
        # index used so far (lower index combinations are already explored).
        self.__solution_map: dict[int, list[int]] = {}
        queue: deque[tuple[int, int]] = deque([(0, 0)])
        while queue:
            target_mask, buttons_pressed = queue.popleft()
            self.__solution_map.setdefault(target_mask, []).append(buttons_pressed)
            for i in range(buttons_pressed.bit_length(), len(self.__buttons)):
                queue.append(
                    (target_mask ^ self.__buttons[i], (1 << i) | buttons_pressed)
                )

    def light_presses(self) -> int:
        return min(s.bit_count() for s in self.__solution_map[self.__light_diagram])

    def joltage_presses(self) -> int:
        presses = self.__joltage_presses(self.__joltage)
        assert presses is not None
        return presses

    def __joltage_presses(self, joltage: list[int]) -> int | None:
        if all(v == 0 for v in joltage):
            return 0
        odd_mask = sum((n % 2) << i for i, n in enumerate(joltage))
        best: int | None = None
        if (solutions := self.__solution_map.get(odd_mask)) is not None:
            for buttons_pressed in solutions:
                remainder = self.__joltage_remainder(buttons_pressed, joltage)
                if (
                    remainder is not None
                    and (rem_cost := self.__joltage_presses(remainder)) is not None
                ):
                    cost = buttons_pressed.bit_count() + 2 * rem_cost
                    best = cost if best is None else min(best, cost)
        return best

    def __joltage_remainder(self, presses: int, joltage: list[int]) -> list[int] | None:
        new_joltages = joltage.copy()
        for idx, button in enumerate(self.__buttons):
            if (presses >> idx) & 1:
                for i, jolt in enumerate(new_joltages):
                    if (button >> i) & 1:
                        if jolt == 0:
                            return None
                        new_joltages[i] -= 1
        return [jolt // 2 for jolt in new_joltages]


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__machines: list[Machine] = [Machine(line) for line in rawstr.splitlines()]

    def get_p1(self) -> int:
        return sum(machine.light_presses() for machine in self.__machines)

    def get_p2(self) -> int:
        return sum(machine.joltage_presses() for machine in self.__machines)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
