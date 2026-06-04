# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        def traverse(node, index):
            nonlocal ans
            if not node:
                return index
            print(node.val, index)
            l = traverse(node.left, index)
            if l >= k:
                return l
            if l + 1 == k:
                ans = node.val
                return l + 1
            return traverse(node.right, l + 1)
        traverse(root, 0)
        return ans