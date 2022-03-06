# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root):
        self.sum=0
        def helper(node):
            if not node: return
            if node.left and node.left.left is None and node.left.right is None:
                self.sum+=node.left.val
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.sum
        
        
        
        '''-------'''
        self.sum = 0
        self.dfs(root, 0)
        return self.sum

    def dfs(self, root, side):
        if not root: return
        
        if not root.left and not root.right:
            if side == -1: self.sum += root.val
        
        self.dfs(root.left, -1)
        self.dfs(root.right, 1)
    