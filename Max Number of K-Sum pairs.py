from collections import defaultdict
from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        res = 0

        for num in nums:
            if freq[k - num] > 0:
                res += 1
                freq[k - num] -= 1
            else:
                freq[num] += 1

        return res
