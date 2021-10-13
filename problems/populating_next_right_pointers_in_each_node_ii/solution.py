"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # level=[root]
        # while root and level:
        #     for i in range(len(level)):
        #         level[i].next=level[i+1] if i+1<len(level) else None
        #     level=[kid for n in level for kid in (n.left,n.right) if kid]
        # return root
        
#         if not root: return None
#         queue=deque([root,None])
#         while queue:
#             node=queue.popleft()
#             if node is None:
#                 if queue:
#                     queue.append(None)
#             else:
#                 node.next=queue[0]
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
                
#         return root


        '''O(1) space'''
        node=root
        while node:
            curr=dummy=Node(0)
            while node:
                if node.left:
                    curr.next=node.left
                    curr=curr.next
                if node.right:
                    curr.next=node.right
                    curr=curr.next
                node=node.next
            node=dummy.next
        return root