# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        '''Recursive'''
        # if root is None:
        #     return False
        # if root.left is None and root.right is None and root.val==targetSum:
        #     return True
        # targetSum-=root.val
        # return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        
        '''Iterative (Stack)'''
        if root is None:
            return False
        stack=[(root,root.val)]
        while stack:
            curr,val=stack.pop()
            if not curr.left and not curr.right and  val==targetSum :
                return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left,val+curr.left.val))
        return False