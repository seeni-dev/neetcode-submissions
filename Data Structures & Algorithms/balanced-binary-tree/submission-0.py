# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# from math import abs

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def isBalancedHelper(root: Optional[TreeNode]):
            if not root:
                return [0, True]
            lHeight = isBalancedHelper(root.left)
            rHeight = isBalancedHelper(root.right)
            if lHeight[1] and rHeight[1] and abs(lHeight[0] - rHeight[0]) <= 1:
                return [max(lHeight[0], rHeight[0])+1, True]
            return [None, False]
        
        return isBalancedHelper(root)[1]
            
            

