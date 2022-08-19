# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque()
        que.append([root,0])
        maxWidth = 0
        
        while que:
            _,start_index = que[0]
            curr_len = len(que)
            end_index = float('-inf')
            for _ in range(curr_len):
                local,end_index = que.popleft()
                
                if local.left:
                    que.append([local.left,2*end_index])
                
                if local.right:
                    que.append([local.right,2*end_index + 1])
            
            maxWidth = max(maxWidth,end_index - start_index + 1)
        return maxWidth
            