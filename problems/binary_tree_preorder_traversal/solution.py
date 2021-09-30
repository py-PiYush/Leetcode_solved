# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        res=[]
        '''---RECURSIVE---'''
#         def preorder(res,root):
#             if root:
#                 res.append(root.val)
#                 preorder(res, root.left)
#                 preorder(res,root.right)
#         preorder(res,root)
        
#         return res
    
        '''---ITERATIVE---'''
        stack=[]
        if not root: return []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                root=root.right
        return res
    