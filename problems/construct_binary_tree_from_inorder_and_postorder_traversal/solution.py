# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         n=len(inorder)
#         if n==0: return None
#         self.inorder=inorder
#         self.postorder=postorder
        
#         return self.build(0,n,0,n)
    
#     def build(self,i_start, i_end, p_start, p_end):
#         if i_start>=i_end or p_start>=p_end:
#             return None
#         root=TreeNode(self.postorder[p_end-1])
#         temp=self.inorder.index(self.postorder[p_end-1])
#         diff=temp-i_start
#         root.left=self.build(i_start,i_start+diff, p_start, p_start+diff)
#         root.right=self.build(i_start+diff+1, i_end, p_start+diff, p_end-1)
        
#         return root

        
        idxMap={v:i for i,v in enumerate(inorder)}
        self.index=len(inorder)-1
        
        def build(left,right):
            if left>right:
                return None
            
            root=TreeNode(postorder[self.index])
            self.index-=1
            
            idx=idxMap[root.val]
            root.right=build(idx+1,right)
            root.left=build(left,idx-1)
            return root
        return build(0,len(inorder)-1)