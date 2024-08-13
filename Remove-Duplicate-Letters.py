class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_index = {char: i for i, char in enumerate(s)}
        
        for i, char in enumerate(s):
            if char not in stack:
                while stack and stack[-1] > char and i < last_index[stack[-1]]:
                    stack.pop()
                stack.append(char)
        
        return ''.join(stack)
