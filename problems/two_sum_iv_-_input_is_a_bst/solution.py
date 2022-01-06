# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        if root.left is None and root.right is None:
            return False
        res=[]
        self.inorder(root, res)
        print(res)
        return self.twoSum(res, k)
    
    def inorder(self,node, res):
        if node:
            self.inorder(node.left, res)
            res.append(node.val)
            self.inorder(node.right, res)
            
    def twoSum(self,lst, target):
        left, right=0,len(lst)-1
        while left<right:
            sum_= lst[left]+lst[right]
            if sum_==target:
                return True
            elif sum_<target:
                left+=1
            else:
                right-=1
        return False
            
        