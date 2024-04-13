from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        players = []
        no, one = [], []
        for win, lose in matches:
            if lose in losses:
                losses[lose] += 1
            else:
                losses[lose] = 1
            players.append(win)
            players.append(lose)
        for player in set(players):
            if losses.get(player, 0) == 0:
                no.append(player)
            elif losses[player] == 1:
                one.append(player)
        no.sort()
        one.sort()
        return [no, one]
