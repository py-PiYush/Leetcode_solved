# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        
        '''Recursive'''
        def helper(root):
            if root:
                if sm.val<=root.val<=lg.val:
                    return root
                elif sm.val<root.val and lg.val<root.val:
                    return helper(root.left)
                else:
                    return helper(root.right)
                
        sm,lg=[p,q] if p.val<q.val else [q,p]
        
        return helper(root)
    
        '''Iterative'''
        # while (root.val-p.val)*(root.val-q.val)>0:
        #     root=(root.left, root.right)[p.val>root.val]
        # return root
            