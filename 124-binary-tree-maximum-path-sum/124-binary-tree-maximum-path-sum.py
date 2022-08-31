# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        self.maxAns = float('-inf')
        
        def maxPathSumHelper(node):
            if not node:
                return 0

            leftSum = max(maxPathSumHelper(node.left),0)
            rightSum = max(maxPathSumHelper(node.right),0)

            ans1 = leftSum + rightSum + node.val

            self.maxAns = max(self.maxAns,ans1)
            
            return node.val + max(leftSum,rightSum)
        
        maxPathSumHelper(root)
        return max(root.val,self.maxAns)
        