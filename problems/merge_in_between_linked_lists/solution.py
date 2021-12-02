# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        l=r=list1
        for i in range(b):
            if i==a-1:
                l=r
            r=r.next
        l.next=list2
        while list2.next:
            list2=list2.next        
        list2.next=r.next
        r.next=None
        return list1
        