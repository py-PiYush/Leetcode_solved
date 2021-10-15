# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        '''Recursive'''
        # node=root
        # if node is None: 
        #     return None
        # if node.val==val:
        #     return node
        # if node.val>val:
        #     n=self.searchBST(node.left,val)
        # elif node.val<val:
        #     n=self.searchBST(node.right, val)
        # return n
    
        '''iterative'''
        
        # stack=[root]
        # while stack:
        #     node=stack.pop()
        #     if node is None:
        #         return None
        #     if node.val==val:
        #         return node
        #     if node.val<val:
        #         stack.append(node.right)
        #     elif node.val>val:
        #         stack.append(node.left)
        # return None
        
        '''No need of stack'''
        curr=root
        while curr:
            if curr.val==val:
                return curr
            elif curr.val<val:
                curr=curr.right
            else:
                curr=curr.left
        return None