# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        
        if root.val == 0 and (left == None and right == None):
            return None
        root.left = left
        root.right = right
        
        return root