"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return None
        
        stack, order=[head], []
        while stack:
            root=stack.pop()
            order.append(root)
            if root.next:
                stack.append(root.next)
            if root.child:
                stack.append(root.child)
            
        for i in range(len(order)-1):
            order[i+1].prev=order[i]
            order[i].next=order[i+1]
            order[i].child=None
        
        return order[0]