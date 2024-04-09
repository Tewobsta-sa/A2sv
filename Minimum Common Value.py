#two pointer method
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i = 0
        j = 0
        min_value = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                return nums1[i]
            elif nums1[i] < nums2[j]:
                i+=1
            else:
                j+=1
        return -1
#using set
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        x = set(nums1)
        y = set(nums2)
        common_elements = x&y
        if not common_elements:
            return -1 
        return min(common_elements)
