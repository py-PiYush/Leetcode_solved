# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return None
        if not k: return head
        front=last=head
        length=1
        while last.next:
            length+=1
            last=last.next
        k%=length
        for _ in range(length-k-1):
            front=front.next
            
        last.next=head
        head=front.next
        front.next=None
        return head
        