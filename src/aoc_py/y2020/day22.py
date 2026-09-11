"""
2020 day 22 - Crab Combat

Kinda straightforward, just a bit messy with the recursion bit, and somewhat slow, can probably be improved by using
dequeue instead of the regular pop.
"""

from copy import deepcopy


class InputData:
    def __init__(self, s: str) -> None:
        self.__players: dict[int, list[int]] = {}
        for i, nbrs in enumerate(s.split("\n\n")):
            self.__players[i] = list(map(int, nbrs.splitlines()[1:]))

    def get_p1(self) -> int:
        players = deepcopy(self.__players)
        while all(len(nbrs) > 0 for nbrs in players.values()):
            draw = [players[p].pop(0) for p in players]
            winner = draw.index(max(draw))
            players[winner].append(draw[winner])
            players[winner].append(draw[(winner + 1) % 2])
        return sum(
            [
                (i + 1) * card
                for i, card in enumerate(
                    reversed(players[0 if len(players[0]) > 0 else 1])
                )
            ]
        )

    def __play_recursive_game(self, players_data: dict[int, list[int]]):
        players = deepcopy(players_data)
        seen: set[str] = set()
        while all(len(nbrs) > 0 for nbrs in players.values()):
            if (current := str(players[0]) + str(players[1])) in seen:
                players[0] += players[1]
                players[1] = []
                return players
            else:
                seen.add(current)
            draw = [players[p].pop(0) for p in players]
            if all(draw[p] <= len(players[p]) for p in players):
                recursive_players = {p: list(players[p][: draw[p]]) for p in players}
                recursion = self.__play_recursive_game(recursive_players)
                winner = 0 if not recursion[1] else 1
            else:
                winner = draw.index(max(draw))
            players[winner].append(draw[winner])
            players[winner].append(draw[(winner + 1) % 2])
        return players

    def get_p2(self) -> int:
        players = deepcopy(self.__players)
        players = self.__play_recursive_game(players)
        return sum(
            [
                (i + 1) * card
                for i, card in enumerate(
                    reversed(players[0 if len(players[0]) > 0 else 1])
                )
            ]
        )


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1, p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
