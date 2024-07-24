# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p and q :
            return False
        if not  q and p:
            return False
        if p.val != q.val:
            return False
        else:
            left = self.isSameTree(p.left, q.left)
            right = self.isSameTree(p.right, q.right)

            return right and left



