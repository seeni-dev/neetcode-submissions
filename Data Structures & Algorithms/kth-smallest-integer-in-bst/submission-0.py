# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = None
        # returns size of root
        def traverse(root: Optional[TreeNode], startIndex: int = 0) -> int:
            nonlocal ans
            if not root:
                return startIndex + 0
            left = traverse(root.left, startIndex)
            if left >= k:
                return left
            currentIndex = left + 1
            if currentIndex == k:
                ans = root.val
            if currentIndex >= k:
                return currentIndex
            return traverse(root.right, currentIndex)
        traverse(root, 0)
        return ans
