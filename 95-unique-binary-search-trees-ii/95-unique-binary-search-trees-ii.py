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
        def generateBST(start,end):
            if start > end:
                return [None]
            ans = []
            for i in range(start,end + 1):
                left = generateBST(start,i - 1)
                right = generateBST(i+1,end)
                
                for l in left:
                    for r in right:
                        curr = TreeNode(i)
                        curr.left = l
                        curr.right = r
                        ans.append(curr)
            
            return ans
        return generateBST(1,n)