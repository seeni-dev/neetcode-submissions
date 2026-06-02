# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -1 * float('inf')
        def dfs(root: Optional[TreeNode]) -> int: # sum of the path using the node. 
            nonlocal ans
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            ans = max(ans, left+right+root.val)
            return root.val + max(left, right)
        dfs(root)
        return ans