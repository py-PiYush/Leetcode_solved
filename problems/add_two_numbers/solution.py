# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = head = ListNode(0)
        carry = 0
        while l1 and l2: 
            val = carry + l1.val + l2.val
            head.next=ListNode(val%10)
            carry = val//10
            l1, l2, head = l1.next, l2.next, head.next
        
        while l1:
            val = carry + l1.val
            head.next = ListNode(val%10)
            carry = val//10
            head, l1 = head.next, l1.next
        
        while l2:
            val = carry + l2.val
            head.next = ListNode(val%10)
            carry = val//10
            head, l2 = head.next, l2.next
        
        if carry:
            head.next=ListNode(carry)
        
        return result.next