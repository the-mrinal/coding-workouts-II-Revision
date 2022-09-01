'''


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.count = 0
        self.secured = {None} # we are keeping none in dict as when node becomes none it will always be secure.
        def dfs(root,parent = None):

            if root is not None:
                dfs(root.left,root)
                dfs(root.right,root)
                
                if (parent is None and root not in self.secured or root.left not in self.secured or root.right not in self.secured): 
                    self.count += 1
                    self.secured.update({parent,root,root.left,root.right})
        
        
        dfs(root)
        return self.count