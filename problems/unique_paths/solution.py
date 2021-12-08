class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        
        '''There are total m+n-2 moves to go from Top-Left to Bottom-Right.
In m+n-2 moves, there are m-1 down moves and n-1 right moves.
You can imagine there are m+n-2 moves as: X X X ... X X X
X can be one of two values: down D or right R.
So, basically, it means we need to calculate how many ways we could choose m-1 down moves from m+n-2 moves, or n-1 right moves from m+n-2 moves.
So total ways = C(m+n-2, m-1) = C(m+n-2, n-1) = (m+n-2)! / (m-1)! / (n-1)!.'''
        return factorial(m+n-2)//factorial(m-1)//factorial(n-1)
        
        
        
        '''(Recursion) TLE'''
#         count=0
#         def path(i,j):
#             nonlocal count
#             if i==m-1 and j==n-1:
#                 count+=1
#                 return
#             if i>=m or j>=n:
#                 return
#             path(i+1,j)
#             path(i,j+1)
        
#         path(0,0)
#         return count
            
        