# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        startS = ""
        destS = ""
        stack = [[root,""]]
        
        while stack:
            curr,path = stack.pop()
            
            if curr.val == startValue:
                startS = path
            
            if curr.val == destValue:
                destS = path
            
            if startS != "" and destS != "":
                break
            
            if curr.left:
                stack.append([curr.left,path + 'L'])
            
            if curr.right:
                stack.append([curr.right,path + 'R'])
        
        while startS and destS and startS[0] == destS[0]:
            startS = startS[1:]
            destS = destS[1:]
        
        return "U"*len(startS) + destS