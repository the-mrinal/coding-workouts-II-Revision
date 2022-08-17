# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        self.ans = 0
        hashMap = defaultdict(int)
        def dfs(node,currSum):
            if not node:
                return 0
            
            currSum += node.val
            if currSum == targetSum:
                self.ans += 1
            
            self.ans += hashMap[currSum - targetSum]
            
            hashMap[currSum] += 1
            
            dfs(node.left,currSum)
            
            dfs(node.right,currSum)
            
            hashMap[currSum] -= 1
        
        dfs(root,0)
        return self.ans