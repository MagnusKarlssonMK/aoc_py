"""
2020 day 22 - Crab Combat

Part 1 is plain Combat: each round both players reveal their top card and the higher card wins both.
Part 2 is recursive Combat: if both players hold at least as many cards as the value they just drew,
the round's winner is decided by a sub-game using those top cards as the starting decks. A game that
would repeat a configuration ends immediately with player 1 winning.

The score of a finished game weights the winning deck's cards by their distance from the bottom.
"""


class InputData:
    def __init__(self, rawstr: str) -> None:
        self.__players: dict[int, list[int]] = {}
        for i, nbrs in enumerate(rawstr.split("\n\n")):
            self.__players[i] = list(map(int, nbrs.splitlines()[1:]))

    @staticmethod
    def __score(players: dict[int, list[int]]) -> int:
        deck = players[0] if players[0] else players[1]
        return sum((i + 1) * card for i, card in enumerate(reversed(deck)))

    def __play_recursive_game(
        self, players_data: dict[int, list[int]]
    ) -> dict[int, list[int]]:
        players = {p: list(cards) for p, cards in players_data.items()}
        seen: set[tuple[tuple[int, ...], tuple[int, ...]]] = set()
        while players[0] and players[1]:
            state = (tuple(players[0]), tuple(players[1]))
            if state in seen:
                players[0] += players[1]
                players[1] = []
                break
            seen.add(state)
            draw = [players[p].pop(0) for p in players]
            if draw[0] <= len(players[0]) and draw[1] <= len(players[1]):
                sub_game = self.__play_recursive_game(
                    {p: players[p][: draw[p]] for p in players}
                )
                winner = 0 if not sub_game[1] else 1
            else:
                winner = draw.index(max(draw))
            players[winner].append(draw[winner])
            players[winner].append(draw[1 - winner])
        return players

    def get_p1(self) -> int:
        players = {p: list(cards) for p, cards in self.__players.items()}
        while players[0] and players[1]:
            draw = [players[p].pop(0) for p in players]
            winner = draw.index(max(draw))
            players[winner].append(draw[winner])
            players[winner].append(draw[1 - winner])
        return self.__score(players)

    def get_p2(self) -> int:
        return self.__score(self.__play_recursive_game(self.__players))


def solve_parts(inputdata: str, part: int | None = None) -> tuple[str, str]:
    p1 = p2 = "-1"
    p = InputData(inputdata)
    if part in (None, 1):
        p1 = str(p.get_p1())
    if part in (None, 2):
        p2 = str(p.get_p2())

    return p1, p2
