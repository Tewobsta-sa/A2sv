class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        i = 0
        j = 0
        new = ''
        while j < len(s):
            if i < len(spaces) and j == spaces[i]:
                new += ' '
                i += 1
            new += s[j]
            j += 1
        return new
