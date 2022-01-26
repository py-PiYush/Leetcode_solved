# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        
        ''' Inorder + timsort '''
        def inorder(node):
            if node:
                inorder(node.left)
                res.append(node.val)
                inorder(node.right)
        res=[]
        inorder(root1)
        inorder(root2)
        return sorted(res)
        
        
        
        
        ''' Inorder traversal + merging O(n+m)'''
        def inorder(node, res):
            if node:
                inorder(node.left, res)
                res.append(node.val)
                inorder(node.right, res)
        
        def merge(a1, a2):
            res=[]
            i,j=0,0
            while i<len(a1) and j<len(a2):
                if a1[i]<=a2[j]:
                    res.append(a1[i])
                    i+=1
                else:
                    res.append(a2[j])
                    j+=1
                
            if i<len(a1):
                res+=a1[i:]
                
            if j<len(a2):
                res+=a2[j:]
                
            return res

        a1, a2 = [], []
        inorder(root1, a1)
        inorder(root2, a2)
        
        return merge(a1, a2)