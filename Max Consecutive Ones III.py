from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        max_len = 0
        zero_count = 0
        for end in range(len(nums)):
            if nums[end] == 0:
                zero_count += 1
                
            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len
