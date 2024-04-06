class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0
        j = 0
        while i < m + j and j < n:
            if nums1[i] > nums2[j]:
                nums1.insert(i, nums2[j])
                nums1.pop()
                j += 1
            i += 1

        # If there are remaining elements in nums2
        while j < n:
            nums1[i] = nums2[j]
            i += 1
            j += 1
