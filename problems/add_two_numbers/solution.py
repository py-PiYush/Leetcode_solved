# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry=0
        sum_=ListNode(0)
        head=sum_
        res=0
        if l1==None and l2==None and carry==0:
            return None
        while l1 or l2:
            res=carry
            if l1:
                res+=l1.val
                l1=l1.next
            if l2:
                res+=l2.val
                l2=l2.next
            value=res%10
            carry=res//10
            sum_.next=ListNode(value)
            sum_=sum_.next
        if carry==1:
            sum_.next=ListNode(carry)
            
       
        return head.next
        