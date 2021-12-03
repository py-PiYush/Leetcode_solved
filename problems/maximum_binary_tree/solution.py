# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        
        '''O(n)'''
        stack = []

        for x in nums:
            n = TreeNode(x)
            while stack and x > stack[-1].val:
                n.left = stack.pop()

            if stack:
                stack[-1].right = n               
            stack.append(n)

        return stack[0]
        
        
        '''O(n^2)'''
        root=TreeNode()
        piv=0
        max_=float('-inf')
        for i in range(len(nums)):
            if nums[i]>max_:
                max_=nums[i]
                piv=i
        root.val=max_
        root.left=self.constructMaximumBinaryTree(nums[0:piv]) if piv>0 else None
        root.right=self.constructMaximumBinaryTree(nums[piv+1:]) if piv<len(nums)-1 else None
        return root