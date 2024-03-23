class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp=[]
        i = 0
        while i < len(nums) - 1:
            if nums[i] == nums[i+1]:
                nums[i] = nums[i]*2
                nums[i+1] = 0
                i+=2
            else:
                i+=1
        new_list =[num for num in nums if num!=0]
        x = nums.count(0)
        return new_list + [0]*x
