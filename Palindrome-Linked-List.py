# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
        
        
