# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indices = {e: i for i, e in enumerate(inorder)}
        
        preOrderIndex = 0
        def dfs(l, r):
            nonlocal preOrderIndex

            if l > r or preOrderIndex >= len(preorder):
                return None
            
            root = TreeNode(preorder[preOrderIndex])
            preOrderIndex+=1
            root.left = dfs(l, indices[root.val] - 1)
            root.right = dfs(indices[root.val]+1, r)
            return root
        return dfs(0, len(inorder)-1)