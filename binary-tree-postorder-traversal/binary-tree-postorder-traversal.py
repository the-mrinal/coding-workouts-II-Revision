# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        out = []
        
        def postOrderRec(root):
            if root is None:
                return
            
            postOrderRec(root.left)
            postOrderRec(root.right)
            out.append(root.val)
            
            return

        
        def postOrderIter(root):
            if root is None:
                return []
            stack,out = [root],[]
            
            while stack:
                curr = stack.pop()
                if curr:
                    out.append(curr.val)
                    stack.append(curr.left)
                    stack.append(curr.right)
            return out[::-1]
            
            
        
        return postOrderIter(root)