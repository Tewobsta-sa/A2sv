class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)
        coins = 0
        i = n - 2
        while i >= n // 3:
            coins += piles[i]
            i -= 2
        return coins
