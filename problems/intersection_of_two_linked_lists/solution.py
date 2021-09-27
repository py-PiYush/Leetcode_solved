# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def skipA(self,pa):
        sa=0
        while pa:
            sa+=1
            pa=pa.next
        return sa
    
    def skipB(self, pb):
        sb=0
        while pb:
            sb+=1
            pb=pb.next
        return sb
    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        
        '''---APPROACH 1---'''
        pa,pb=headA, headB
#         sa,sb=0,0
#         while True:
#             if pa is None:
#                 sb=self.skipB(pb)
#                 break
#             elif pb is None:
#                 sa=self.skipA(pa)
#                 break
#             pa=pa.next
#             pb=pb.next
        
#         pa,pb=headA, headB
#         if sa:
#             while sa:
#                 pa=pa.next
#                 sa-=1
#         if sb:
#             while sb:
#                 pb=pb.next
#                 sb-=1
                
#         while pa and pb:
#             if pa==pb:
#                 return pa
#             pa=pa.next
#             pb=pb.next
        
        
    
    
        '''---BETTER---'''
        # while pa!=pb:
        #     pa=pa.next if pa else headB
        #     pb=pb.next if pb else headA
        # return pa
    
    
        '''---USING SET---'''
        seen=set()
        while pa:
            seen.add(pa)
            pa=pa.next
        while pb:
            if pb in seen:
                return pb
            pb=pb.next
        
            