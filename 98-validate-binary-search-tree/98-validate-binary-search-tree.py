# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node,lower,upper):
            if not node:
                return True
            left = validate(node.left,lower,node.val)
            right = validate(node.right,node.val,upper)
            
            if left and right and node.val > lower and node.val < upper:
                return True
            return False
        return validate(root,float('-inf'),float('inf'))