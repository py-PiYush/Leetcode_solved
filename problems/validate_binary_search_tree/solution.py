# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
#         def validate(node, low=-math.inf, high=math.inf):
#             if not node:
#                 return True
#             if node.val<=low or node.val>=high:
#                 return False
#             return validate(node.left,low,node.val) and validate(node.right, node.val, high)
        
#         return validate(root)
    
    
        '''Iterative inorder traversal'''
        stack,prev=[], -math.inf
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            root=stack.pop()
            if root.val<=prev:
                return False
            prev=root.val
            root=root.right
        return True
        
        
        
        
        '''Wrong'''
        # if root:
        #     left =self.isValidBST(root.left)
        #     right= self.isValidBST(root.right)
        #     if left and right:
        #         if root.left and root.right and not (root.left.val<root.val or root.right.val>root.val):
        #             return False
        #         if root.left and not root.left.val<root.val:
        #             return False
        #         if root.right and not root.val<root.right.val:
        #             return False
        #         return True
        #     return False
        # return True
            