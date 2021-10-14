from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        '''Iterative (bfs)'''
#         if p is None and q is None: return True
#         if p is None or q is None: return False
        
#         queue=collections.deque([p,q])
#         while queue:
#             node1,node2=queue.popleft(), queue.popleft()
#             if node1 is None and node2 is None:
#                 continue
#             if node1 is None or node2 is None:
#                 return False
#             if node1.val!=node2.val:
#                 return False
            
#             queue+=[node1.left, node2.left, node1.right, node2.right]
#         return True
    
        '''Recursion'''
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val!=q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            