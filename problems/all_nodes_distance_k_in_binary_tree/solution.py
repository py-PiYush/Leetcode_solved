# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par=par
                dfs(node.left, node)
                dfs(node.right, node)
        
        dfs(root)
        q=deque([(target, 0)])
        seen={target}
        while q:
            if q[0][1]==k:
                return [node.val for node, d in q]
            node, d = q.popleft()
            for n in (node.left, node.right, node.par):
                if n and n not in seen:
                    seen.add(n)
                    q.append((n, d+1))
        return []