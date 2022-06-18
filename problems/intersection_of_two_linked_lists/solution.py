# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        '''---APPROACH 1---'''
        pa,pb=headA, headB
        while pa and pb:
            if pa==pb:
                return pa
            pa = pa.next
            pb = pb.next
        
        diff = headA if pa else headB
        pointer = pa if pa else pb
        
        while pointer:
            diff = diff.next
            pointer = pointer.next
        
        pointer2=headB if pa else headA
        
        while diff and pointer2:
            if diff == pointer2:
                return diff
            diff=diff.next
            pointer2=pointer2.next
        return None
    
    
        '''---BETTER---'''
        # while pa!=pb:
        #     pa=pa.next if pa else headB
        #     pb=pb.next if pb else headA
        # return pa
    
    
        '''---USING SET---'''
        # seen=set()
        # while pa:
        #     seen.add(pa)
        #     pa=pa.next
        # while pb:
        #     if pb in seen:
        #         return pb
        #     pb=pb.next
        
            