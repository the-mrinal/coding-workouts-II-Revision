# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        return self.helper(1,n)
    
    
    def helper(self,start,end):
        if start > end:
            return [None]
        ans = []
        for curr in range(start,end + 1):
            
            left = self.helper(start,curr - 1)
            right = self.helper(curr+1,end)
            
            for l in left:
                for r in right:
                    node = TreeNode(curr)
                    node.left = l
                    node.right = r
                    ans.append(node)
            
        return ans