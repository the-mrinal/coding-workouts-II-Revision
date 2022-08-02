# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverse(node):
            prev = None
            curr = node
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        def merge(nodeA,nodeB):
            finalHead = ListNode(None)
            ansNode = finalHead
            
            while nodeA and nodeB:
                temp = nodeA.next
                temp2 = nodeB.next
                nodeA.next = nodeB
                ansNode.next = nodeA
                ansNode = ansNode.next.next
                nodeA = temp
                nodeB = temp2
            if nodeA:
                ansNode.next = nodeA
            if nodeB:
                ansNode.next = nodeB
            return finalHead.next
        
        slow = head
        fast = head
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        istNode = slow
        iindNode = slow.next
        istNode.next = None
        iindNode = reverse(iindNode)
        
        return merge(head,iindNode)