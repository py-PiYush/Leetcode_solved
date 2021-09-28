# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # print(head.val)
        # if head==None or head.next==None:
        #     return head
        # p=self.reverseList(head.next)
        # print(head.val)
        # head.next.next=head
        # head.next=None
        # return p
        
        prev=None
        
        while head:
            curr=head
            head=head.next
            curr.next=prev
            prev=curr
        return prev
        