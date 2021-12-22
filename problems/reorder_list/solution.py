# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        
        
        '''TLE'''
        def find_mid(node):
            fast,slow=node,node
            while fast.next and fast.next.next:
                fast=fast.next.next
                slow=slow.next
            return slow
        
        def reverse(node):
            prev=None
            while node:
                curr=node
                node=node.next
                curr.next=prev
                prev=curr
            return prev
        
        
        mid=find_mid(head)
        n2=reverse(mid.next)
        mid.next=None
        n1=head
        
        
        while n2:
            print(n1.val, n2.val)
            temp=n1.next
            n1.next=n2
            n1=n2
            n2=temp
