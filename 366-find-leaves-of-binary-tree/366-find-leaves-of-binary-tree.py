# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        ans = []
        
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if max(left,right) == len(ans):
                ans.append([])
            
            ans[max(left,right)].append(node.val)
            
            return max(left,right) + 1
        
        dfs(root)
        return ans