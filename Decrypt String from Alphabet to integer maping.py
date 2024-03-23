class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        char = []
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                ch = 96 + int(s[i:i+2])
                i += 3
            else:
                ch = 96 + int(s[i])
                i += 1
            char.append(chr(ch))
        return ''.join(char)
