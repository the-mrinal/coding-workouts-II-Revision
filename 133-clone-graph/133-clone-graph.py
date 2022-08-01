"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        cache = {}
        def clone(main_node):
            nonlocal cache
            if not node:
                return None
            
            if main_node not in cache:

                clone_node = Node(main_node.val,[])
                cache[main_node] = clone_node
                
                for child in main_node.neighbors:
                    clone_node.neighbors.append(clone(child))
                
            return cache[main_node]
        
        return clone(node)