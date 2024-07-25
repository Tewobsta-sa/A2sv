# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        ahead = dummy
        behind = dummy
        while n > 0:
            ahead = ahead.next
            n-=1
        while ahead.next:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return dummy.next
