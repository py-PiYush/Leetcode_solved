from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         res=[]
#         queue=deque([])
#         if root:
#             queue.append(root)
        
#         while len(queue):
#             level=[]
#             for _ in range(len(queue)):
#                 x=queue.popleft()
#                 level.append(x.val)
#                 if x.left:
#                     queue.append(x.left)
#                 if x.right:
#                     queue.append(x.right)
#             res.append(level)
#         return res
            
    
    
        res,level=[],[root]
        while root and level:
            res.append([x.val for x in level])
            level=[kid for n in level for kid in (n.left, n.right) if kid]
        return res
            
            
            