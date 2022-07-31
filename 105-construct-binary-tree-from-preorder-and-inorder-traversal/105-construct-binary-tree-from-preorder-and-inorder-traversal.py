# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
inorder 
left root right

preorder
root left right


root = preorder[0]

def findRootInorder(val):
    index = 
    root.left = inorder[:index]
    root.right = inorder[index +1:]
    
node = TreeNode(root)
for i in range(len(preorder)):
    index = inorder.index(val)
    node.left = inorder[:index]
    node.right = inoredr[index+1:]

'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def helper(start,end):
            nonlocal preOrderIndex,index_map
            if start > end:
                return None
            
            val = preorder[preOrderIndex]
            
            index = index_map[val]
            
            root = TreeNode(val)
            
            preOrderIndex += 1
            
            root.left = helper(start,index - 1)
            root.right = helper(index + 1,end)
            
            return root
        
        preOrderIndex = 0
        
        index_map = {val:index for index,val in enumerate(inorder)}
        
        return helper(0,len(inorder) - 1)
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            