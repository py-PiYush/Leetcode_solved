# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        
        '''---USING SET---'''
        # seen=set()
        # temp=head
        # while temp:
        #     if temp in seen:
        #         return temp
        #     else:
        #         seen.add(temp)
        #     temp=temp.next
        # return None
        
        '''---TWO POINTER---
            O(1) memory    
        '''
        slow,fast=head,head
        while fast:
            if fast.next is None:
                return None
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        if fast is None:
            return None
            
        slow=head
        while slow:
            if slow==fast:
                return slow
            slow=slow.next
            fast=fast.next