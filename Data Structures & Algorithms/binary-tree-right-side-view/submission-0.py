# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = []
        if root:
            q = [root]
        while q:
            nq = []
            if q:
                res.append(q[-1].val)
            for e in q:
                if e.left:
                    nq.append(e.left)
                if e.right:
                    nq.append(e.right)
            q = nq
        return res
        