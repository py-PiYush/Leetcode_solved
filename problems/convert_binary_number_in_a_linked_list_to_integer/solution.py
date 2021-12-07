# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        num=0
        while head:
            num=(num<<1)|head.val
            head=head.next
        return num
        
        
        
        
        
        ''''''
        str_=''
        while head!=None:
            str_+=str(head.val)
            head=head.next
        return((int(str_,2)))
        