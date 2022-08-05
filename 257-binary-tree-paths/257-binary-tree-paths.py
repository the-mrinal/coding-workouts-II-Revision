class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        def dfs(root):
            stack = [[root, str(root.val)]]
            
            while stack:
                curr,path = stack.pop()
                
                if not curr.left and not curr.right:
                    ans.append(path)
                    continue
                
                if curr.right:
                    stack.append([curr.right,path + "->" + str(curr.right.val)])
                if curr.left:
                    stack.append([curr.left,path + "->" + str(curr.left.val)])
        dfs(root)
        return ans
                    