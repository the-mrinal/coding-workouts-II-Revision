# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count = 0
        currA = headA
        currB = headB
        
        while currA and currB and count < 2:
            if currA == currB:
                return currA
            
            if currA.next:
                currA = currA.next
            else:
                currA = headB
                count += 1
            
            if currB.next:
                currB = currB.next
            else:
                currB = headA
            
        
        return None