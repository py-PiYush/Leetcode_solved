from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        queue=deque([])
        if root:
            queue.append(root)
        
        while len(queue):
            level=[]
            for _ in range(len(queue)):
                x=queue.popleft()
                level.append(x.val)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
            res.append(level)
        return res
            