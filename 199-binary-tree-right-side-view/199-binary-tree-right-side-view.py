# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        que = deque()
        
        if root:
            que.append([root,0])
        
        result = []
        currLevel = 0
        prev = None
        while que:
            curr,level = que.popleft()
            
            if level != currLevel:
                currLevel = level
                result.append(prev.val)
            prev = curr
            
            if curr.left:
                que.append([curr.left,level + 1])

            
            if curr.right:
                que.append([curr.right,level + 1])
        
        if prev:
            result.append(prev.val)
        
        return result