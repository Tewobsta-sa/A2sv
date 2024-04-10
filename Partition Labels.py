class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        result = []
        end = 0
        size = 0
        for i in range(len(s)):
            last[s[i]]=i
        for i in range(len(s)):
            end= max(end,last[s[i]])
            size += 1
            if i == end:
                result.append(size)
                size = 0
        return result
#more optimized code
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        start = 0
        end = 0
        last_index = 0
        result = []

        for i in range(len(s)):
            last_index = max(last_index, last[s[i]])
            if i == last_index:
                result.append(end - start + 1)
                start = end + 1
            end += 1

        return result
