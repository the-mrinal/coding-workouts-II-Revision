# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''


'''

class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        res = []
        def traverse(node):
            nonlocal res
            if not node:
                return None
            left = traverse(node.left)
            right = traverse(node.right)
            node.left = left
            node.right = right
            if node.val in to_delete:
                if left:
                    res.append(left)
                if right:
                    res.append(right)
                node = None
            return node
            
        ans = traverse(root)
        if ans:
            res.append(ans)
        return res
                