# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        if head:
            nxt = head.next
        new_head = head
        while curr and curr.next and nxt:
            print(curr.val,nxt.val)
            curr.next = nxt.next
            nxt.next = curr
            if not prev:
                new_head = nxt
            else:
                prev.next = nxt
            
            prev = curr
            curr = curr.next
            if curr:
                nxt = curr.next
            else:
                nxt = None       
        
        return new_head