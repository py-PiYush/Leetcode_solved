"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def post(node):
            if node:
                for n in node.children:
                    post(n)
                res.append(node.val)
        
        # print([node.val for node in root.children])
        res = []
        post(root)
        return res