# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        mid = self.middleNode(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.mergeTwoLists(left, right)
    
    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        midPrev=None
        while head and head.next:
            if midPrev is not None: 
                midPrev=midPrev.next
            else:
                midPrev=head
            head=head.next.next
        
        mid = midPrev.next
        midPrev.next=None
        return mid
    
    
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list=temp=ListNode(0)
        
        while l1 and l2:
            
            if l1.val<=l2.val:
                temp.next=l1
                
                l1=l1.next
            else:
                temp.next=l2
                
                l2=l2.next
            temp=temp.next
            
        temp.next = l1 or l2
        return list.next