# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        '''Recursion (first approach)'''
#         self.root=root
#         node=root
#         def helper(node, val):
#             if val<node.val:
#                 if node.left is None:
#                     node.left=TreeNode(val)
#                     return self.root
#                 else:
#                     return helper(node.left, val)
                
#             elif val>node.val :
#                 if node.right is None:
#                     node.right= TreeNode(val)
#                     return self.root
#                 else:
#                     return helper(node.right, val)
#         if root is None:
#             return TreeNode(val)
#         return helper(node, val)

        '''Better Recursion'''
        if root is None:
            return TreeNode(val)
        if val>root.val:
            root.right=self.insertIntoBST(root.right, val)
        elif val<root.val:
            root.left=self.insertIntoBST(root.left, val)
        return root
    
        '''Iterative'''
        curr=root
        if curr is None:
            return TreeNode(val)
        while curr:
            if val<curr.val:
                if curr.left is None:
                    curr.left=TreeNode(val)
                    return root
                else:
                    curr=curr.left
            if val>curr.val:
                if curr.right is None:
                    curr.right=TreeNode(val)
                    return root
                else:
                    curr=curr.right
            
            
