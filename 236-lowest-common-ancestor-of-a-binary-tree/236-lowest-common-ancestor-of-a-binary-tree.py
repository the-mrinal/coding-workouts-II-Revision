# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.ans = None
    
    
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def findLCA(node):
            if node is None:
                return False
            
            left = findLCA(node.left)
            right = findLCA(node.right)
            
            mid = node == p or node == q
            
            if int(mid) + int(left) + int(right) >= 2:
                self.ans = node
                
            return mid or left or right
        findLCA(root)
        return self.ans