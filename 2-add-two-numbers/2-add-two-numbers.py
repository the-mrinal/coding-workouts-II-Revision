# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        newHead = ListNode(None)
        totalSum = newHead
        
        while l1 or l2:
            l1Val = 0
            l2Val = 0
            if l1:
                l1Val = l1.val
            if l2:
                l2Val = l2.val
            currSum = l1Val + l2Val + carry
            carry = currSum // 10
            currSum = currSum % 10
            totalSum.next = ListNode(currSum)
            totalSum = totalSum.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if carry:
            totalSum.next = ListNode(carry)
            
        return newHead.next