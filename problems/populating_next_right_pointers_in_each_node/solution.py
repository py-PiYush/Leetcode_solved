"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # res=[]
        # level=[root]
        # while root and level:
        #     for i in range(len(level)):
        #         level[i].next=level[i+1] if i+1<len(level) else None
        #     level=[kid for n in level for kid in (n.left,n.right) if kid]
        # return root
        
        '''O(1) space'''
        head=root
        while root and root.left:
            next=root.left
            while root:
                root.left.next=root.right
                root.right.next=root.next.left if root.next else None
                root=root.next
            root=next
        return head