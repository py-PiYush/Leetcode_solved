# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ahead, behind=head, head
        prev=None
        for _ in range(n):
            ahead=ahead.next
        
        while ahead:
            ahead=ahead.next
            prev=behind
            behind=behind.next
        if not prev:
            head=behind.next
        else:
            prev.next=behind.next
        return head
        