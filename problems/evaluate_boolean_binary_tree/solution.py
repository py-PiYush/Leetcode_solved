# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if root.left is None:
            return root.val
        if root.val==2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
            
        # val1 = self.evaluateTr
        # ee(root.left)
        # val2 = self.evaluateTree(root.right)
        # if root.val == 2:
        #     return val1 or val2
        # else:
        #     return val1 and val2
        # # return val1 (and, or)[root.val == 2] val2
        