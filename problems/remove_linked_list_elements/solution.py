# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        cur = head
        dummy.next = cur
        while cur:
            if cur.val == val:
                prev.next = cur.next
                cur = prev.next
            else:
                prev = cur
                cur = cur.next
        return dummy.next
        
        # dummy = curr = ListNode(-1)
        # curr.next=head
        # while curr.next:
        #     if curr.next.val==val:
        #         curr.next=curr.next.next
        #     else:
        #         curr=curr.next
        # return dummy.next
    
    
        #<--------------recursive--------->
        
#         if not head:
#             return None
        
#         if head.val == val:
#             return self.removeElements(head.next, val)
#         else:
#             head.next = self.removeElements(head.next, val)
#             return head  
            