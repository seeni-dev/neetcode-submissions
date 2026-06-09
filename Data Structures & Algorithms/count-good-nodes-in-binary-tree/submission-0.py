# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import bisect

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0
        def countGoodNodes(node: TreeNode, path: List[int]) -> int:
            nonlocal counter
            if not node:
                return
            if not path or path[-1] <= node.val:
                counter += 1
            bisect.insort_left(path, node.val)
            countGoodNodes(node.left, path)
            countGoodNodes(node.right, path)
            toDeleteIndex = bisect.bisect_left(path, node.val)
            if toDeleteIndex in range(len(path)):
                del path[toDeleteIndex]
        countGoodNodes(root, [])
        return counter
        