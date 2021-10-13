# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
#         inorderTravList=[]
#         def inorder(root, inorderTravList):
#             if root is None:
#                 return None
#             inorder(root.left, inorderTravList)
#             inorderTravList.append(root.val)
#             inorder(root.right, inorderTravList)
            
#         inorder(root, inorderTravList)
#         idx1=inorderTravList.index(p.val)
#         idx2=inorderTravList.index(q.val)
#         sm,lg=(idx1, idx2) if idx1<idx2 else (idx2,idx1)
#         queue=[root]
#         while queue:
#             node=queue.pop(0)
#             if node:
#                 if node.val in inorderTravList[sm:lg+1]:
#                     return node
#                 queue.append(node.left)
#                 queue.append(node.right)

        '''Recursive'''
#         self.lca=0
#         def helper(node):
#             if not node:
#                 return False
#             left=helper(node.left)
#             right=helper(node.right)
#             mid=node==p or node==q
            
#             if mid+left+right>=2:
#                 self.lca=node
#             return mid or left or right
#         helper(root)
#         return self.lca
    
        '''Iterative '''
        parent={root:None}
        stack=[root]
        while p not in parent or q not in parent:
            node=stack.pop()
            if node.left:
                parent[node.left]=node
                stack.append(node.left)
            if node.right:
                parent[node.right]=node
                stack.append(node.right)
        ancestors=set()
        while p:
            ancestors.add(p)
            p=parent[p]
        while q not in ancestors:
            q=parent[q]
        return q
            