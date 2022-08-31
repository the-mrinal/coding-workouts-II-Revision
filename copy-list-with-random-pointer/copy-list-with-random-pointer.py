"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    
    def __init__(self):
        self.cache = {}
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        if head in self.cache:
            return self.cache[head]
        
        cloneH = Node(head.val)
        self.cache[head] = cloneH
        
        cloneH.random = self.copyRandomList(head.random)
        cloneH.next = self.copyRandomList(head.next)
        return cloneH