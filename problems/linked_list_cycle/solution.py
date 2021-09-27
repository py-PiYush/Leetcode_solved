# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        '''--- USING SET---'''
        seen=set()
        temp=head
        while temp:
            if temp in seen:
                return True
            else:
                seen.add(temp)
            temp=temp.next
        return False
        
        
        '''---TWO POINTER---'''
#         slow,fast=head,head
        
#         while fast:
#             if fast.next is None:
#                 return False
#             fast=fast.next.next
#             slow=slow.next
#             if slow==fast:
#                 return True
            
#         return False
        