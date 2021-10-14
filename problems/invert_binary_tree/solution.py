from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''Recursion'''
        # if root is None: return None
        # temp=root.left
        # root.left=root.right
        # root.right=temp
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root
        
        '''Bottom up recursion'''
        # if root is None: return None
        # right=self.invertTree(root.right)
        # left=self.invertTree(root.left)
        # root.left=right
        # root.right=left
        # return root
        
        '''Iterative'''
        # if root is None: return None
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     if node:
        #         node.left,node.right=node.right, node.left
        #         stack.append(node.left)
        #         stack.append(node.right)
        # return root
        
        '''Iterative bfs'''
        if root is None: return None
        queue=deque([root])
        while queue:
            node=queue.popleft()
            node.left,node.right = node.right, node.left
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        return root