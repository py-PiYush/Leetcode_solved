# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        
        '''---RECURSIVE---'''
        # def postorder(res,root):
        #     if root:
        #         postorder(res,root.left)
        #         postorder(res,root.right)
        #         res.append(root.val)
        # postorder(res,root)
        # return res
        
        '''---ITERATIVE---'''
        stack=[root]
        while stack:
            temp=stack.pop()
            if temp:
                if isinstance(temp,TreeNode):
                    stack.append(temp.val)
                    stack.append(temp.right)
                    stack.append(temp.left)
                else:
                    res.append(temp)
        return res
                