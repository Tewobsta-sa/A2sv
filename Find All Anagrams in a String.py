from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(p)
        initial = 0
        window = s[initial:n]
        x = Counter(p)
        y = Counter(window)
        result = []
        
        if x == y:
            result.append(initial)
        
        for i in range(len(s) - n):
            initial += 1
            n += 1
            y[s[initial - 1]] -= 1
            if y[s[initial - 1]] == 0:
                del y[s[initial - 1]]
            if s[n - 1] in y:
                y[s[n - 1]] += 1
            else:
                y[s[n - 1]] = 1
            
            if x == y:
                result.append(initial)
                
        return result
