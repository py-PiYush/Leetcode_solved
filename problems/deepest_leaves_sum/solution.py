# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def dfs1(node):
            if not node: return 0
            return max(dfs1(node.left), dfs1(node.right)) + 1
        
        def dfs2(node, d):
            if not node: return
            if d == depth: self.ans += node.val
            dfs2(node.left, d+1)
            dfs2(node.right, d+1)
        
        self.ans = 0
        depth = dfs1(root)
        dfs2(root, 1)
        return self.ans