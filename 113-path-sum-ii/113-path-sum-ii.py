# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        stack = []
        if root:
            stack.append([root,[root.val]])
        res = []
        while stack:
            curr,path = stack.pop()
            
            if not curr.right and not curr.left:
                if sum(path) == targetSum:
                    res.append(path.copy())
            
            if curr.left:
                stack.append([curr.left,path + [curr.left.val]])
            
            if curr.right:
                stack.append([curr.right,path + [curr.right.val]])
        
        return res