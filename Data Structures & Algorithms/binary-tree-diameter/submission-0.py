# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def traverse(root):
            nonlocal ans
            if not root:
                return 0
            left = traverse(root.left)
            right = traverse(root.right)
            ans = max(ans, left + 1 + right)
            return max(left, right) + 1 
        traverse(root)
        return ans - 1