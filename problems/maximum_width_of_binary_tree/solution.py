# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:     
        ans, deque = 0, collections.deque()
        deque.append((root, 0))

        while deque:
            ans = max(ans, deque[-1][1] - deque[0][1] + 1)

            qlen = len(deque)
            for i in range(qlen):
                node, index = deque.popleft()
                if node.left:
                    deque.append((node.left, 2 * index))
                if node.right:
                    deque.append((node.right, 2 * index + 1))

        return ans
        