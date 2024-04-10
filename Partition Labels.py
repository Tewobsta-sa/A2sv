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
