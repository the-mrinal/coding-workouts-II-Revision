"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        stack = []
        curr = root
        prev = None
        new_head = None
        
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop()
            
            if prev is None:
                new_head = curr
            else:
                prev.right = curr
            
            curr.left = prev
            prev = curr
            
            curr = curr.right
        
        new_head.left = prev
        prev.right = new_head
        
        return new_head