# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = head
        curr = head
        count = 0
        
        while curr:
            curr = curr.next
            if count == n + 1:
                prev = prev.next
            else:
                count += 1
        
        if count == n:
            return prev.next
        
        if  prev.next:
            prev.next = prev.next.next
        
        return head