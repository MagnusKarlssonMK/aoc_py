"""
2015 day 15 - Science for Hungry People

Generates the different quantity combinations through recursion, with just an additional constraint
for part 2. Calculates the results for both parts in one go, since all combinations anyhow need to be
explored for both.
"""


class InputData:
    __TOTAL_INGREDIENTS = 100
    __CALORIE_MAX = 500

    def __init__(self, s: str) -> None:
        self.__ingredients: list[list[int]] = []
        for line in s.splitlines():
            w = line.split()
            self.__ingredients.append(
                list(
                    map(
                        int,
                        [
                            w[2].rstrip(","),
                            w[4].rstrip(","),
                            w[6].rstrip(","),
                            w[8].rstrip(","),
                            w[10],
                        ],
                    )
                )
            )

    def __solve_recipe(self, remaining: int, quantities: list[int]) -> tuple[int, int]:
        if len(quantities) == len(self.__ingredients) - 1:
            # We are at the last ingredient - assign the remainder
            new_quantities = quantities + [remaining]

            score = 1
            for idx in range(4):
                score *= max(
                    0,
                    sum(
                        q * self.__ingredients[i][idx]
                        for i, q in enumerate(new_quantities)
                    ),
                )

            # Calorie check for part 2
            cal_score = score
            calories = sum(
                self.__ingredients[i][4] * q for i, q in enumerate(new_quantities)
            )
            if calories != self.__CALORIE_MAX:
                cal_score = 0

            return score, cal_score
        else:
            # Recursion by trying all possible quantities for the next ingredient
            max_score_p1 = 0
            max_score_p2 = 0
            for q in range(remaining + 1):
                quantities.append(q)
                scores = self.__solve_recipe(remaining - q, quantities)
                max_score_p1 = max(max_score_p1, scores[0])
                max_score_p2 = max(max_score_p2, scores[1])
                quantities.pop()

            return max_score_p1, max_score_p2

    def get_scores(self) -> tuple[int, int]:
        return self.__solve_recipe(self.__TOTAL_INGREDIENTS, [])


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    r1, r2 = p.get_scores()
    if part in (None, 1):
        p1 = str(r1)
    if part in (None, 2):
        p2 = str(r2)

    return p1, p2
