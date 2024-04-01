class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * (max(nums)+1)
        for num in nums:
            count[num] += 1
        target = 0
        for index, value in enumerate(count):
            for i in range(value):
                nums[target] = index
                target += 1
#you can use any sorting algorithm or just the sort function as shown below
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
