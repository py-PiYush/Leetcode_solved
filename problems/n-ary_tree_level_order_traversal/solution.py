"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        if not root:
            return []
        paths = [[root.val]]
        queue=deque([root])
        while queue:
            path=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                for c in node.children:
                    path.append(c.val)
                    queue.append(c)
            if path:
                paths.append(path)
        return paths
        
        
        '''--------------------------------------'''
        res,level=[],[root]
        while root and level:
            res.append([x.val for x in level])
            level=[kid for n in level for kid in n.children if kid]
        return res
            
        