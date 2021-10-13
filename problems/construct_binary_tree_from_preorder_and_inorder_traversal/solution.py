# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idxMap={v:i for i,v in enumerate(inorder)}
        self.index=0
        
        def build(left,right):
            if left>right:
                return None
            root=TreeNode(preorder[self.index])
            self.index+=1
            idx=idxMap[root.val]
            root.left=build(left,idx-1)
            root.right=build(idx+1,right)
            return root
        
        return build(0,len(inorder)-1)