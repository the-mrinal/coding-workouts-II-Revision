# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def findLeftHeight(self,root:Optional[TreeNode]):
        count = 0
        curr = root
        while curr:
            count += 1
            curr = curr.left
        return count
    def findRightHeight(self,root:Optional[TreeNode]):
        count = 0
        curr = root
        while curr:
            count += 1
            curr = curr.right
        return count
    
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        leftH = self.findLeftHeight(root)
        rightH = self.findRightHeight(root)
        
        if leftH == rightH:
            return (2**leftH) - 1
        ans1 = self.countNodes(root.left)
        ans2 = self.countNodes(root.right)
        
        return 1 + ans1 + ans2