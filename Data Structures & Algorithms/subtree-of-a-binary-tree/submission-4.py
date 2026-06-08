# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], equalityOnly: Bool = False) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False
        
        t = root.val == subRoot.val
        if t:
            t = self.isSubtree(root.left, subRoot.left, True) and self.isSubtree(root.right, subRoot.right, True)
        if not t and equalityOnly:
            return False
        if not t:
            t = self.isSubtree(root.left, subRoot)
        if not t:
            t = self.isSubtree(root.right, subRoot)
        return t
