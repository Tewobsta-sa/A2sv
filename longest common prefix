class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        prefix = ""
        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break
        return prefix
