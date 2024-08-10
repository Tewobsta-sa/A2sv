class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(bit_string):
            return ''.join('1' if ch == '0' else '0' for ch in bit_string)
        
        s = ["0"]
        for i in range(1, n):
            s.append(s[i-1] + "1" + ''.join(reversed(invert(s[i-1]))))
        
        return s[n-1][k-1]
