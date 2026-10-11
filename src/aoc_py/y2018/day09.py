"""
2018 day 9 - Marble Mania
"""

from collections import deque


class InputData:
    __MULTIPLE = 23
    __REMOVE = 7

    def __init__(self, s: str) -> None:
        w = s.split()
        self.__nbr_players = int(w[0])
        self.__last_marble = int(w[6])

    def get_winning_score(self, marble_multiplier: int = 1) -> int:
        scores = [0] * self.__nbr_players
        marble_circle = deque([0])
        for marble in range(1, (self.__last_marble * marble_multiplier) + 1):
            if marble % InputData.__MULTIPLE != 0:
                marble_circle.rotate(-1)
                marble_circle.append(marble)
            else:
                marble_circle.rotate(InputData.__REMOVE)
                player = marble % self.__nbr_players
                scores[player] += marble + marble_circle.pop()
                marble_circle.rotate(-1)
        return max(scores)


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_winning_score())
    if part in (None, 2):
        p2 = str(p.get_winning_score(100))

    return p1, p2
