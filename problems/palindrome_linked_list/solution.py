# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''---REVERSE AND COMPARE---'''
#     def isPalindrome(self, head: Optional[ListNode]) -> bool:
#         node=head
#         # node=node.next
#         # self.printList(head)
#         list_clone=self.clone(node)
#         # self.printList(list_clone)
        
#         self.printList(head)
#         print('')
#         reversed=self.reverse(list_clone)
#         self.printList(head)
#         # self.printList(reversed)
#         # self.printList(head)
#         return self.isEqual(head, reversed)
    
#     def clone(self,node):
#         new=dummy=ListNode(0)
#         while node:
#             new.next=node
#             node=node.next
#             new=new.next
#         return dummy.next
    
#     def reverse(self, node):
#         prev=None
#         curr=node
#         while curr:
#             next_node=curr.next
#             curr.next=prev
#             prev=curr
#             curr=next_node
#         return prev
    
#     def isEqual(self, node1, node2):
#         while node1 and node2:
#             if node1.val!=node2.val:
#                 return False
#             return True
        
#     def printList(self, node):
#         while node:
#             print(node.val, end=' ')
#             node=node.next


    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        # Find the end of first half and reverse second half.
        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # Check whether or not there's a palindrome.
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False
            first_position = first_position.next
            second_position = second_position.next

        # Restore the list and return the result.
        first_half_end.next = self.reverse_list(second_half_start)
        return result    

    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous
        