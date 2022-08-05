# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def reverse(node):
            curr = node
            prev = None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        
        prev_n = head
        curr_n = head
        count = 0
        newNode = ListNode(None)
        newHead = newNode
        
        while curr_n:
            # print(count,'f')
            if count == k - 1:
                count = 0
                temp = curr_n.next
                curr_n.next = None
                newHead.next = reverse(prev_n)
                while newHead.next:
                    newHead = newHead.next
                prev_n = temp
                curr_n = temp
            else:
                count += 1
                curr_n = curr_n.next
        
        if prev_n:
            newHead.next = prev_n
        
        return newNode.next