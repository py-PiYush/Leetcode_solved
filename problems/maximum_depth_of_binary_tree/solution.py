# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        '''---TOP-DOWN---'''
        def top_down(root,depth,answer): 
            if not root:
                return
            if not root.left and not root.right:
                answer[0]=max(answer[0],depth)
            top_down(root.left,depth+1,answer)
            top_down(root.right,depth+1,answer)

        
        depth=1
        answer=[0]
        top_down(root,depth,answer)
        return answer[0]

        '''---BOTTOM-UP---'''
        # if not root:
        #     return 0
        # left_depth=self.maxDepth(root.left)
        # right_depth=self.maxDepth(root.right)
        # return max(left_depth,right_depth)+1
#         