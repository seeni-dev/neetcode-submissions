import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBSTHelper(self, root: Optional[TreeNode], lower_bound, upper_bound) -> bool:
        if not root:
            return True
        if not (lower_bound < root.val < upper_bound):
            return False
        return self.isValidBSTHelper(root.left, lower_bound, root.val) and \
                self.isValidBSTHelper(root.right, root.val, upper_bound)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isValidBSTHelper(root, float('inf') * -1 , float('inf'))
        