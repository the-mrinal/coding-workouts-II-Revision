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
        st = []
        curr = root
        prev = None
        head = None
        
        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left
            
            curr = st.pop()
            if prev is None:
                curr.left = prev
                head = curr
            else:
                curr.left = prev
                prev.right = curr
            
            prev = curr
            curr = curr.right
        
        
        prev.right = head
        head.left = prev
        
        return head