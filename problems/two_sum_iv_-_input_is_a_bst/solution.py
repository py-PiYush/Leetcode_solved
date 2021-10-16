# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
            
        def inorder(root):
            if root:
                left=inorder(root.left)
                if (k-root.val) in set_:
                    return True
                set_.add(root.val)
                right=inorder(root.right)
                return left or right
            
        def preorder(root):
            if root:
                if k-root.val in set_:
                    return True
                set_.add(root.val)
                return preorder(root.left) or preorder(root.right)

        set_=set()
       
      
        return preorder(root)
        
        