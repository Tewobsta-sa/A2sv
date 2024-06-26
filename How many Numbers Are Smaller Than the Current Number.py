class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0] * len(nums)
        for i in range(len(nums)):
            for num in nums:
                if num < nums[i]:
                    count[i] += 1
        return count
