import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        i = 0
        j = int(math.sqrt(c))
        j_squared = j ** 2

        while i <= j:
            current_sum = i ** 2 + j_squared
            if current_sum == c:
                return True
            elif current_sum < c:
                i += 1
            else:
                j -= 1
                j_squared = j ** 2

        return False
